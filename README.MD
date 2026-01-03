# Django Bookstore REST API

A simple bookstore / library backend REST API built with Django and Django REST Framework.  
This project was created for exam and portfolio purposes, focusing on clean architecture,
relational data modeling, and RESTful API design.

## Project Goals

The goal of this project is to implement a well-structured and maintainable backend system
that demonstrates:

- Management of multiple related data models
- REST API built with Django REST Framework
- Django Admin interface for full data management
- Separation of concerns (models, serializers, views)
- API usability via the DRF Browsable API

## Technologies Used

- Python 3
- Django
- Django REST Framework
- Database: MySQL

Note: For local development, a different database (e.g. SQLite) can be used if configured
in `settings.py`.

## Project Structure

```text
bookstore-exam/
├── bookstore/                      # Project configuration
│   ├── __init__.py
│   ├── asgi.py                     # ASGI configuration
│   ├── settings.py                 # Global settings (DB, apps, etc.)
│   ├── urls.py                     # Root URL routing
│   └── wsgi.py                     # WSGI configuration
│
├── library/                        # Application (app)
│   ├── migrations/                 # Database migrations
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py                    # Admin interface configuration
│   ├── apps.py                     # App configuration
│   ├── models.py                   # Models (Author, Category, Book)
│   ├── serializers.py              # DRF serializers
│   ├── views.py                    # ViewSets / API logic
│   ├── urls.py                     # App-specific routing
│   └── tests.py                    # Tests (optional)
│
├── postman/                        # Postman collection and API tests
├── screenshot/                     # Screenshots
├── .gitignore
├── db.sqlite3                      # Local development database
├── manage.py
├── README.md
└── requirements.txt                # Python dependencies
```

## Data Models

### Author
- first_name
- middle_name (nullable)
- last_name
- created_at
- updated_at

### Category
- name
- description
- is_active
- created_at
- updated_at

### Book
- title
- published_date
- price (CHF)
- stock
- author (ForeignKey)
- category (ForeignKey)
- created_at
- updated_at

### Computed / denormalized fields in API responses
- author_first_name
- author_middle_name
- author_last_name
- category_name
- is_available (derived from stock)

## REST API

The API is available under the api/ prefix.

Author Endpoints
	•	GET /api/authors/ – list all authors
	•	GET /api/authors/<id>/ – retrieve author details

Category Endpoints
	•	GET /api/categories/ – list all categories
	•	GET /api/categories/<id>/ – retrieve category details

Book Endpoints
	•	GET /api/books/ – list all books
	•	GET /api/books/<id>/ – retrieve book details

Note:
The API is read-only. Write operations (POST, PUT, PATCH, DELETE) are intentionally not enabled.

Admin Interface
	•	Admin URL: http://127.0.0.1:8000/admin/
	•	All models are accessible via the Django admin interface
	•	Admin configuration is located in library/admin.py

Installation and Setup

1) Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

2) Install dependencies
pip install -r requirements.txt

3) Run database migrations
python manage.py makemigrations
python manage.py migrate

4) Create an admin user
python manage.py createsuperuser

5) Start the development server
python manage.py runserver

### Included screenshots

- `admin-author-list.png` – Author management in Django Admin
- `admin-category-list.png` – Category list with active status
- `admin-book-create.png` – Creating a book with related author and category
- `admin-book-category-select.png` – ForeignKey category selection
- `admin-book-author-select.png` – ForeignKey author selection
- `api-root.png` – API root with available endpoints
- `api-books-list.png` – Book list REST endpoint (GET)
- `api-categories-list.png` – Category list REST endpoint (GET)