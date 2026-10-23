# Level 3 - Python Development Tasks

## Task 1: Django Authentication Web Application

### Project Overview

This project is a web application built with Django that allows users to register, log in, access a protected dashboard, and log out securely.

### Features

* User registration with username, email, and password.
* User login and logout.
* Password validation using Django's authentication system.
* Protected dashboard accessible only to authenticated users.
* Automatic redirection to the login page when an unauthenticated user attempts to access the dashboard.
* SQLite database for storing user information.

### Technologies Used

* Python
* Django
* SQLite
* HTML

### Project Structure

```text
level_3/
├── auth_system/
│   ├── templates/
│   │   └── auth_system/
│   │       ├── register.html
│   │       ├── login.html
│   │       └── dashboard.html
│   ├── forms.py
│   ├── urls.py
│   └── views.py
├── config/
│   ├── settings.py
│   └── urls.py
├── manage.py
└── db.sqlite3
```

### How to Run the Project

1. Navigate to the `level_3` directory.

2. Activate the virtual environment from the project root:

   ```powershell
   ..\.venv\Scripts\Activate.ps1
   ```

3. Install Django if it is not already installed:

   ```powershell
   python -m pip install django
   ```

4. Apply database migrations:

   ```powershell
   python manage.py migrate
   ```

5. Start the development server:

   ```powershell
   python manage.py runserver
   ```

6. Open the application in your browser:

   * Home/Login: http://127.0.0.1:8000/
   * Registration: http://127.0.0.1:8000/auth_system/register/
   * Dashboard: http://127.0.0.1:8000/auth_system/

### Learning Outcomes

* Understanding Django project and application structure.
* Implementing user registration and authentication.
* Working with Django forms and templates.
* Protecting routes with authentication decorators.
* Connecting a Django application to a database.
* Configuring URL routing and redirects.
