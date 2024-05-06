# Django Telegram Clone

This project is a simple clone of the popular messaging application Telegram, implemented using Django and Django REST Framework.

## Description

The Django Telegram Clone project aims to replicate the core functionalities of Telegram, allowing users to send and receive messages, manage their contacts. It provides RESTful API endpoints for communication between clients and the server.

## Requirements

- Python 3.x
- Django 3.x
- Django REST Framework
- PostgreSQL (or other compatible database)
- (Optional) Channels for websockets support

## Setup

Follow these steps to set up and run the Django Telegram Clone project:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/django-telegram-clone.git
cd django-telegram-clone
```

### 2. Clone the repository

```bash
pip install -r requirements.txt
```

### 3. Configure the Database
Edit the `settings.py` file in the `telegram` directory to configure the database settings:

```python
# settings.py
   
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Replace `your_database_name`, `your_database_user`, and `your_database_password` with your actual database credentials.


### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

### 6. Access the application
Open your web browser and go to `http://localhost:8000` to access the application.


### 6. Access the application
Enjoy

### 8. License
This project is licensed under the MIT License - see the LICENSE file for details.