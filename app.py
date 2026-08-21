from flask import Flask, render_template, request, url_for, session, make_response, redirect
import mysql.connector
app = Flask(__name__)

app.secret_key = "dfvsadknfoenrfcoaef"

# Home
@app.route("/")
def index():

    username = request.cookies.get("username")

    return render_template("index.html", username = username )


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if  request.method == 'POST':

        username = request.form["username"]

        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO users (username) VALUES (%s)",
            (username,)
        )
        db.commit()
        cursor.close()

        # store username in session
        session['username'] = username

        # create response
        response = make_response(
            redirect(url_for('dashboard'))
        )

        response.set_cookie(
            "username",
            username,
            max_age=60* 60* 24*7
        )

        return response

    return render_template('login.html')


# Dashboard
@app.route("/dashboard")
def dashboard():

    if "username"  not in session:
        return redirect(url_for('login'))

    username = session["username"]

    return render_template(
        "dashboard.html",
        username = username
    )

# logout
@app.route("/logout")
def logout():

    # remove the username from session
    session.pop("username", None)

    return redirect(url_for("index"))

# Delete cookie
@app.route("/delete-cookie")
def delete_cookie():

    response = make_response(
        redirect(url_for("index"))
    )

    response.delete_cookie("username")

    return response

# Databases connection

db = mysql.connector.connect(
    host = 'localhost',
    user='root',
    password='root',
    database='flask_db'
)

if db.is_connected():
    print("Successfully connected from mysql")



if __name__ == "__main__":
    app.run(debug=True)


    