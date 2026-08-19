# 🐍 Flask — Basic to Advanced

A complete learning roadmap for **Flask**, starting from the fundamentals and progressing to advanced and production-level concepts.

---

## 📚 Flask Roadmap

```text
Flask Basics
     ↓
Application
     ↓
Routes
     ↓
HTTP Methods
     ↓
Request & Response
     ↓
URL Parameters
     ↓
Query Parameters
     ↓
JSON
     ↓
Templates
     ↓
Jinja2
     ↓
Forms
     ↓
Cookies & Sessions
     ↓
Error Handling
     ↓
Blueprints
     ↓
Application Factory
     ↓
Configuration
     ↓
Database
     ↓
SQLAlchemy
     ↓
CRUD
     ↓
Relationships
     ↓
Authentication
     ↓
Authorization
     ↓
REST API
     ↓
Validation
     ↓
File Upload
     ↓
Pagination
     ↓
Middleware
     ↓
Decorators
     ↓
Testing
     ↓
Logging
     ↓
Caching
     ↓
Background Tasks
     ↓
Security
     ↓
Production
```

---

# 1. What is Flask?

Flask is a lightweight Python web framework.

It can be used to build:

- Web applications
- REST APIs
- Backend applications
- Microservices

Basic Flask flow:

```text
Client
   ↓
Request
   ↓
Flask
   ↓
Route
   ↓
Python Function
   ↓
Response
```

---

# 2. Installation

Check Python:

```bash
python --version
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate on Windows:

```bash
venv\Scripts\activate
```

Activate on Linux/macOS:

```bash
source venv/bin/activate
```

Install Flask:

```bash
pip install flask
```

Check Flask:

```bash
flask --version
```

---

# 3. First Flask Application

Create:

```text
app.py
```

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"


if __name__ == "__main__":
    app.run(debug=True)
```

Run:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

# 4. Flask Application Object

The application is created using:

```python
app = Flask(__name__)
```

`app` represents your Flask application.

You use it to:

- Create routes
- Configure the application
- Register blueprints
- Register error handlers
- Register extensions

---

# 5. Routes

A route connects a URL to a Python function.

```python
@app.route("/")
def home():
    return "Home Page"
```

Another route:

```python
@app.route("/about")
def about():
    return "About Page"
```

URLs:

```text
/
/about
```

---

# 6. Dynamic Routes

You can put values inside URLs.

```python
@app.route("/user/<name>")
def user(name):
    return f"Hello {name}"
```

URL:

```text
/user/Abhay
```

Response:

```text
Hello Abhay
```

---

## Typed URL Parameters

Integer:

```python
@app.route("/user/<int:id>")
def get_user(id):
    return f"User ID: {id}"
```

Other converters:

```text
string
int
float
path
uuid
```

Example:

```python
@app.route("/product/<int:id>")
def product(id):
    return f"Product {id}"
```

---

# 7. HTTP Methods

HTTP methods define what the client wants to do.

```text
GET       → Read
POST      → Create
PUT       → Update
PATCH     → Partial Update
DELETE    → Delete
```

Example:

```python
@app.route("/users", methods=["GET"])
def get_users():
    return "Get users"


@app.route("/users", methods=["POST"])
def create_user():
    return "Create user"


@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    return f"Update user {id}"


@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    return f"Delete user {id}"
```

---

# 8. Request Object

Import:

```python
from flask import request
```

The `request` object contains information sent by the client.

```text
request
├── args
├── form
├── json
├── files
├── cookies
├── headers
└── method
```

---

# 9. Query Parameters

Example URL:

```text
/search?name=Abhay&age=22
```

Code:

```python
@app.route("/search")
def search():

    name = request.args.get("name")
    age = request.args.get("age")

    return {
        "name": name,
        "age": age
    }
```

---

# 10. JSON Request

Client sends:

```json
{
    "name": "Abhay",
    "email": "abhay@example.com"
}
```

Flask:

```python
@app.route("/users", methods=["POST"])
def create_user():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")

    return {
        "name": name,
        "email": email
    }
```

---

# 11. JSON Response

Flask can return a dictionary:

```python
@app.route("/api/user")
def user():

    return {
        "id": 1,
        "name": "Abhay",
        "role": "Developer"
    }
```

Flask converts it into JSON.

---

# 12. Response Object

You can create custom responses.

```python
from flask import jsonify

@app.route("/users")
def users():

    response = jsonify({
        "message": "Users found"
    })

    return response, 200
```

---

# 13. HTTP Status Codes

Common status codes:

| Code | Meaning |
|---|---|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 409 | Conflict |
| 500 | Server Error |

Example:

```python
return {
    "message": "User created"
}, 201
```

---

# 14. Templates

Flask can render HTML.

Project:

```text
project/
│
├── app.py
│
└── templates/
    └── index.html
```

Python:

```python
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")
```

HTML:

```html
<!DOCTYPE html>
<html>

<head>
    <title>Flask</title>
</head>

<body>

    <h1>Hello Flask</h1>

</body>

</html>
```

---

# 15. Jinja2

Flask uses Jinja2 for templates.

Python:

```python
@app.route("/")
def home():

    name = "Abhay"

    return render_template(
        "index.html",
        name=name
    )
```

HTML:

```html
<h1>Hello {{ name }}</h1>
```

---

## Jinja Conditions

```html
{% if user %}
    <h1>Hello {{ user.name }}</h1>
{% else %}
    <h1>Please login</h1>
{% endif %}
```

---

## Jinja Loops

```html
<ul>

{% for user in users %}

    <li>{{ user.name }}</li>

{% endfor %}

</ul>
```

---

# 16. Static Files

Project:

```text
project/
│
├── app.py
│
├── templates/
│   └── index.html
│
└── static/
    ├── css/
    │   └── style.css
    │
    └── js/
        └── script.js
```

HTML:

```html
<link
    rel="stylesheet"
    href="{{ url_for('static', filename='css/style.css') }}"
>
```

---

# 17. Forms

HTML:

```html
<form method="POST">

    <input
        type="text"
        name="username"
    >

    <button type="submit">
        Submit
    </button>

</form>
```

Flask:

```python
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")

        return f"Hello {username}"

    return render_template("login.html")
```

---

# 18. Cookies

Set a cookie:

```python
from flask import make_response


@app.route("/set-cookie")
def set_cookie():

    response = make_response("Cookie set")

    response.set_cookie(
        "username",
        "Abhay"
    )

    return response
```

Read cookie:

```python
@app.route("/get-cookie")
def get_cookie():

    username = request.cookies.get("username")

    return username
```

---

# 19. Sessions

Sessions store user-specific information.

```python
from flask import session
```

Set secret key:

```python
app.secret_key = "your-secret-key"
```

Store data:

```python
session["username"] = "Abhay"
```

Read data:

```python
username = session.get("username")
```

Remove:

```python
session.pop("username", None)
```

---

# 20. Redirect

Use:

```python
from flask import redirect
```

Example:

```python
@app.route("/old")
def old():

    return redirect("/new")
```

---

# 21. URL Building

Use:

```python
from flask import url_for
```

Example:

```python
@app.route("/")
def home():
    return "Home"


@app.route("/profile")
def profile():
    return "Profile"


@app.route("/go")
def go():

    return redirect(
        url_for("profile")
    )
```

---

# 22. Error Handling

Handle 404:

```python
@app.errorhandler(404)
def not_found(error):

    return {
        "error": "Page not found"
    }, 404
```

Handle 500:

```python
@app.errorhandler(500)
def server_error(error):

    return {
        "error": "Internal server error"
    }, 500
```

---

# 23. Custom Exceptions

You can create your own exceptions:

```python
class UserNotFound(Exception):
    pass
```

Then handle them:

```python
@app.errorhandler(UserNotFound)
def handle_user_not_found(error):

    return {
        "error": "User not found"
    }, 404
```

---

# 24. Project Structure

For a larger Flask application:

```text
flask_app/
│
├── app/
│   │
│   ├── __init__.py
│   │
│   ├── routes/
│   │   ├── users.py
│   │   ├── auth.py
│   │   └── products.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── product.py
│   │
│   ├── services/
│   │   ├── user_service.py
│   │   └── auth_service.py
│   │
│   ├── templates/
│   │
│   └── static/
│
├── tests/
│
├── config.py
├── run.py
├── requirements.txt
├── .env
└── .gitignore
```

---

# 25. Blueprints

Blueprints allow you to split your Flask application into modules.

Example:

```python
from flask import Blueprint

user_bp = Blueprint(
    "users",
    __name__
)


@user_bp.route("/users")
def users():

    return {
        "users": []
    }
```

Register:

```python
app.register_blueprint(user_bp)
```

You can create separate blueprints for:

```text
auth
users
products
orders
admin
```

---

# 26. Application Factory

Instead of creating the application globally:

```python
app = Flask(__name__)
```

use:

```python
def create_app():

    app = Flask(__name__)

    return app
```

Example:

```python
from flask import Flask


def create_app():

    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello Flask"

    return app
```

Benefits:

- Easier testing
- Better configuration
- Multiple environments
- Better project organization
- Easier extension initialization

---

# 27. Configuration

Create:

```python
class Config:

    SECRET_KEY = "secret"

    DEBUG = True
```

Load configuration:

```python
app.config.from_object(Config)
```

Different configurations can be created for:

```text
Development
Testing
Production
```

---

# 28. Environment Variables

Never store secrets directly in code.

Bad:

```python
SECRET_KEY = "my-secret"
```

Use environment variables:

```text
SECRET_KEY=your-secret
DATABASE_URL=your-database-url
```

Access:

```python
import os

secret = os.getenv("SECRET_KEY")
```

---

# 29. Database

Flask doesn't force you to use one specific database.

Common choices:

```text
SQLite
PostgreSQL
MySQL
```

For Python applications, SQLAlchemy is commonly used as an ORM.

Install:

```bash
pip install flask-sqlalchemy
```

---

# 30. SQLAlchemy

Initialize:

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

Model:

```python
class User(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )
```

---

# 31. Database CRUD

## Create

```python
user = User(
    name="Abhay",
    email="abhay@example.com"
)

db.session.add(user)
db.session.commit()
```

## Read

```python
users = User.query.all()
```

Find by ID:

```python
user = db.session.get(User, 1)
```

## Update

```python
user = db.session.get(User, 1)

user.name = "New Name"

db.session.commit()
```

## Delete

```python
user = db.session.get(User, 1)

db.session.delete(user)
db.session.commit()
```

---

# 32. Database Relationships

Learn:

```text
One-to-One
One-to-Many
Many-to-Many
```

Example:

```text
User
  ↓
Posts
```

One user can have many posts.

```python
class Post(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.String(200)
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id")
    )
```

---

# 33. Database Migrations

Learn Flask-Migrate for managing database schema changes.

Install:

```bash
pip install flask-migrate
```

Typical workflow:

```bash
flask db init
flask db migrate
flask db upgrade
```

Migrations are important when your database structure changes over time.

---

# 34. REST API

A REST API exposes resources through HTTP.

Example:

```text
GET    /api/users
POST   /api/users
GET    /api/users/1
PUT    /api/users/1
DELETE /api/users/1
```

Think:

```text
GET       → Read
POST      → Create
PUT       → Update
DELETE    → Delete
```

---

# 35. CRUD API Example

```python
@app.route("/api/users", methods=["GET"])
def get_users():

    users = User.query.all()

    return [
        {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
        for user in users
    ]
```

Create:

```python
@app.route("/api/users", methods=["POST"])
def create_user():

    data = request.get_json()

    user = User(
        name=data["name"],
        email=data["email"]
    )

    db.session.add(user)
    db.session.commit()

    return {
        "message": "User created"
    }, 201
```

---

# 36. Authentication

Authentication answers:

> Who are you?

Common flow:

```text
Register
   ↓
Hash Password
   ↓
Store User
   ↓
Login
   ↓
Verify Password
   ↓
Create Session/Token
```

Never store plain-text passwords.

Use:

```python
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
```

Hash:

```python
password_hash = generate_password_hash(
    password
)
```

Verify:

```python
check_password_hash(
    password_hash,
    password
)
```

---

# 37. Authorization

Authorization answers:

> What are you allowed to do?

Example:

```text
User
Admin
Moderator
```

An admin may be allowed to:

```text
Create users
Delete users
Manage products
View admin dashboard
```

A normal user may not have those permissions.

---

# 38. JWT Authentication

JWT can be used for API authentication.

Flow:

```text
Login
  ↓
Verify Credentials
  ↓
Create JWT
  ↓
Client Stores Token
  ↓
Client Sends Token
  ↓
Flask Verifies Token
  ↓
Protected Endpoint
```

Header:

```text
Authorization: Bearer <token>
```

---

# 39. Request Validation

Never trust incoming data.

Validate:

```text
Required fields
Data types
Email
String length
Number ranges
Allowed values
```

Useful libraries:

```text
Pydantic
Marshmallow
```

Example validation concept:

```python
if not data.get("email"):

    return {
        "error": "Email is required"
    }, 400
```

---

# 40. Pagination

Don't return thousands of database records at once.

Example:

```text
GET /users?page=1&limit=20
```

Response:

```json
{
    "data": [],
    "page": 1,
    "limit": 20,
    "total": 100
}
```

Learn:

```text
Pagination
Filtering
Sorting
Searching
```

---

# 41. File Upload

Receive a file:

```python
@app.route("/upload", methods=["POST"])
def upload():

    file = request.files.get("file")

    if not file:

        return {
            "error": "File required"
        }, 400

    file.save(
        f"uploads/{file.filename}"
    )

    return {
        "message": "File uploaded"
    }
```

Learn security considerations such as:

```text
Allowed extensions
File size limits
Safe filenames
File type validation
```

---

# 42. Decorators

Flask uses decorators heavily.

Example:

```python
@app.route("/")
def home():
    return "Home"
```

You can also create custom decorators.

Example:

```python
from functools import wraps


def login_required(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print("Checking authentication")

        return function(*args, **kwargs)

    return wrapper
```

Use:

```python
@login_required
def profile():

    return "Profile"
```

---

# 43. Middleware

Middleware allows logic to run around requests.

Concept:

```text
Request
   ↓
Middleware
   ↓
Route
   ↓
Response
   ↓
Middleware
   ↓
Client
```

Flask provides hooks such as:

```python
@app.before_request
def before_request():

    print("Request received")
```

And:

```python
@app.after_request
def after_request(response):

    return response
```

---

# 44. Sessions

Sessions are useful for keeping information between requests.

```python
session["user_id"] = 10
```

Read:

```python
user_id = session.get("user_id")
```

Remove:

```python
session.pop("user_id", None)
```

---

# 45. Testing

Install:

```bash
pip install pytest
```

Test:

```python
def test_home(client):

    response = client.get("/")

    assert response.status_code == 200
```

Test:

```text
Routes
API
Authentication
CRUD
Validation
Errors
Database
```

---

# 46. Logging

Use Python logging:

```python
import logging

logging.basicConfig(
    level=logging.INFO
)

logging.info("Application started")
```

Useful logging levels:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

---

# 47. Caching

Caching stores frequently used data temporarily.

Architecture:

```text
Client
  ↓
Flask
  ↓
Cache
  ↓
Database
```

Redis is commonly used for caching.

Learn:

```text
Cache
Cache expiration
Cache invalidation
Redis
```

---

# 48. Background Tasks

Some tasks take too long to execute during a normal HTTP request.

Examples:

```text
Email sending
Report generation
Large file processing
Data processing
Scheduled jobs
```

A common architecture:

```text
Flask
  ↓
Task Queue
  ↓
Worker
  ↓
Background Task
```

Celery is commonly used with Flask for background tasks.

---

# 49. Security

Important Flask security concepts:

```text
Password hashing
Authentication
Authorization
Input validation
SQL injection prevention
CSRF protection
Secure cookies
CORS
Rate limiting
File upload security
Secret management
HTTPS
```

Never trust client input.

---

# 50. Production Configuration

Development:

```text
DEBUG=True
```

Production:

```text
DEBUG=False
```

Never expose debugging information in production.

Use environment variables for:

```text
SECRET_KEY
DATABASE_URL
API_KEYS
JWT_SECRET
```

---

# 51. Gunicorn

Flask's development server should not be used as your production server.

Install:

```bash
pip install gunicorn
```

Run:

```bash
gunicorn app:app
```

For an application factory:

```bash
gunicorn "app:create_app()"
```

---

# 52. Docker

A basic Dockerfile:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
```

Build:

```bash
docker build -t flask-app .
```

Run:

```bash
docker run -p 8000:8000 flask-app
```

---

# 53. Production Architecture

A typical Flask deployment:

```text
                 Internet
                    ↓
                  Nginx
                    ↓
                Gunicorn
                    ↓
                  Flask
                 /     \
                ↓       ↓
          PostgreSQL    Redis
                          ↓
                       Celery
```

---

# 54. Health Check

Create:

```python
@app.route("/health")
def health():

    return {
        "status": "ok"
    }, 200
```

This can be used to check whether your application is running.

---

# 55. Advanced Project Structure

```text
flask_app/
│
├── app/
│   │
│   ├── __init__.py
│   ├── extensions.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── products.py
│   │   └── orders.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── product.py
│   │   └── order.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   └── order_service.py
│   │
│   ├── schemas/
│   │   └── user_schema.py
│   │
│   └── utils/
│       └── helpers.py
│
├── tests/
│   ├── test_auth.py
│   ├── test_users.py
│   └── test_products.py
│
├── migrations/
├── config.py
├── run.py
├── requirements.txt
├── Dockerfile
├── .env
├── .gitignore
└── README.md
```

---

# 56. Flask Learning Projects

## 🟢 Beginner

### Project 1 — Hello Flask

Learn:

```text
Application
Routes
Request
Response
```

---

### Project 2 — Calculator

Build:

```text
/add
/subtract
/multiply
/divide
```

Learn:

```text
Routes
URL parameters
Query parameters
HTTP responses
```

---

## 🟡 Intermediate

### Project 3 — Todo API

Build:

```text
POST   /todos
GET    /todos
GET    /todos/<id>
PUT    /todos/<id>
DELETE /todos/<id>
```

Learn:

```text
CRUD
JSON
Database
SQLAlchemy
Validation
```

---

### Project 4 — User Authentication

Build:

```text
POST /register
POST /login
GET  /profile
POST /logout
```

Learn:

```text
Password hashing
Sessions
JWT
Authentication
Authorization
```

---

## 🟠 Advanced

### Project 5 — Blog API

Features:

```text
Users
Posts
Comments
Likes
Authentication
Authorization
Database relationships
Pagination
Search
Filtering
```

---

### Project 6 — E-Commerce API

Features:

```text
Users
Products
Categories
Cart
Orders
Authentication
Authorization
Pagination
Search
Filtering
File uploads
```

---

# 57. Flask Checklist

## Beginner

- [ ] What is Flask?
- [ ] Install Flask
- [ ] Create Flask application
- [ ] Routes
- [ ] Dynamic routes
- [ ] HTTP methods
- [ ] Request object
- [ ] Response object
- [ ] Query parameters
- [ ] URL parameters
- [ ] JSON

## Intermediate

- [ ] Templates
- [ ] Jinja2
- [ ] Static files
- [ ] Forms
- [ ] Cookies
- [ ] Sessions
- [ ] Redirects
- [ ] Error handling
- [ ] Blueprints
- [ ] Configuration
- [ ] Environment variables
- [ ] SQLAlchemy
- [ ] CRUD
- [ ] Relationships
- [ ] Database migrations

## Advanced

- [ ] REST API design
- [ ] Authentication
- [ ] Authorization
- [ ] JWT
- [ ] Validation
- [ ] Custom decorators
- [ ] Middleware
- [ ] Pagination
- [ ] File uploads
- [ ] Testing
- [ ] Logging
- [ ] Caching
- [ ] Background tasks
- [ ] Security
- [ ] Application Factory

## Production

- [ ] Production configuration
- [ ] Gunicorn
- [ ] Nginx
- [ ] Docker
- [ ] Health checks
- [ ] Logging
- [ ] Monitoring
- [ ] Database migrations
- [ ] HTTPS
- [ ] Deployment

---

# 🎯 Final Goal

After completing this roadmap, you should be able to build a complete Flask application:

```text
                    Flask Application
                           │
             ┌─────────────┼─────────────┐
             ↓             ↓             ↓
          Routes        Services       Models
             │             │             │
             └─────────────┼─────────────┘
                           ↓
                        Database
                           │
             ┌─────────────┴─────────────┐
             ↓                           ↓
          Redis                        Celery
             │                           │
          Caching                  Background Tasks
```

The most important thing is to **build projects while learning**.

Don't just memorize Flask syntax.

Understand this flow:

```text
Request
   ↓
Route
   ↓
Validation
   ↓
Authentication
   ↓
Business Logic
   ↓
Database
   ↓
Response
```

Once you understand this flow, you can build real Flask applications from scratch.