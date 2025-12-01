###Prodev Backend API

A Django-based REST API for managing a product catalog with user authentication. This project supports CRUD operations, pagination, filtering, sorting, and secure JWT-based authentication. It comes with mock data and a custom registration page.

##Features

#User Authentication

#JWT-based authentication

#User registration via API or custom HTML page

#Custom user model with profile photo and date of birth

#Catalog Management

#Products and categories with full CRUD operations

#Filtering products by category

#Sorting products by price

#Pagination for large datasets

#Seed Data

#10 categories

#150 products (enough for pagination and filtering demonstration)

#Optional test users

#API Documentation

#Accessible via Swagger (/api/docs/) and Redoc (/api/redoc/)

#Dockerized

#Runs Django backend and MySQL database in separate containers

#Simplifies setup and deployment

##Requirements

Python 3.10+

Django 4.x

Django REST Framework

MySQL

Docker & Docker Compose (optional but recommended)

Node.js (optional for frontend customization)

###Setup

1. Clone the Repository
   git clone <repo_url>
   cd Prodev_backend

2. Environment Variables

Create a .env file in the root directory:

MYSQL_DATABASE=prodev_db
MYSQL_USER=prodev_user
MYSQL_PASSWORD=secret123
MYSQL_ROOT_PASSWORD=root123
SECRET_KEY=your_django_secret_key
DEBUG=True

3. Install Dependencies
   pip install -r requirements.txt

4. Database

If using MySQL without Docker:

Create the database and user in MySQL Workbench or CLI.

Update .env accordingly.

##Docker Setup

Run the project in Docker:

docker-compose up --build

Backend API: http://localhost:8000

MySQL: localhost:3306

Swagger docs: http://localhost:8000/api/docs/

Docker handles:

Django migrations

Static files collection

Running the backend with Gunicorn

Database persistence via Docker volume

##Database Seeding

Populate the database with mock data:

python manage.py seed_users
python manage.py seed_catalogue

Users will be created for testing authentication.

Products and categories will be generated automatically for pagination and filtering.

##API Endpoints
##Authentication

#Register

POST /api/users/register/

Body (JSON):

{
"username": "kevin",
"email": "kevin@example.com",
"password": "TestPass123",
"password2": "TestPass123",
"first_name": "Kevin",
"last_name": "Nshuti"
}

Returns JWT tokens for the new user.

Obtain Token

POST /api/auth/token/

Body:

{
"username": "kevin",
"password": "TestPass123"
}

Refresh Token

POST /api/auth/token/refresh/

Body:

{
"refresh": "<refresh_token>"
}

###Catalogue

##Products

GET /api/products/ – List products (supports pagination, filtering, sorting)

POST /api/products/ – Create product (requires JWT)

GET /api/products/<id>/ – Retrieve product

PUT/PATCH /api/products/<id>/ – Update product (requires JWT)

DELETE /api/products/<id>/ – Delete product (requires JWT)

##Categories

GET /api/categories/ – List categories

POST /api/categories/ – Create category (requires JWT)

GET /api/categories/<slug>/ – Retrieve category

PUT/PATCH /api/categories/<slug>/ – Update category (requires JWT)

DELETE /api/categories/<slug>/ – Delete category (requires JWT)

###Using the API
##With cURL

Register a user

curl -X POST http://localhost:8000/api/auth/register/ \
-H "Content-Type: application/json" \
-d '{
"username": "kevin",
"email": "kevin@example.com",
"password": "TestPass123",
"password2": "TestPass123",
"first_name": "Kevin",
"last_name": "Nshuti"
}'

Obtain JWT Token

curl -X POST http://localhost:8000/api/auth/token/ \
-H "Content-Type: application/json" \
-d '{
"username": "kevin",
"password": "TestPass123"
}'

Use Token in Requests

curl -H "Authorization: Bearer <access_token>" \
http://localhost:8000/api/products/

With Postman

Import API endpoints from /api/docs/ Swagger JSON.

Use the register or token endpoints to create users and obtain tokens.

Add Authorization: Bearer <access_token> header to access protected routes.

Custom User Registration Page

Accessible at /register/

Submits data to /api/auth/register/ via JavaScript

Displays success or error messages dynamically

Uses HTML/CSS for a modern, appealing design

###Docker

Purpose:

Runs backend and database in isolated containers.

Simplifies deployment and ensures a consistent environment.

Handles migrations, static files, and Gunicorn server automatically.

Commands:

Start containers:

docker-compose up --build

Stop containers:

docker-compose down

Next Steps: Deployment

The backend can be deployed on cloud providers like Heroku, AWS Elastic Beanstalk, DigitalOcean, or Vercel for APIs.

Docker ensures the same environment is portable.

We can configure:

Environment variables for production

HTTPS via Nginx or cloud load balancers

Persistent database volumes for MySQL

This README now includes everything: Docker, seed data, API usage with cURL/Postman, user registration, and catalog operations.
