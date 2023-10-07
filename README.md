This is a Django-based backend system designed to provide user registration, authentication, and content posting functionality. This project serves as an example of building a robust backend system using Django and related technologies.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
  - [User Registration](#user-registration)
  - [Authentication](#authentication)
  - [Creating Posts](#creating-posts)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [License](#license)

## Getting Started

### Prerequisites

Before running the project, make sure you have the following prerequisites installed:

- Python (3.10+)
- Django (4.2+)
- PostgreSQL (15.0+)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Django SimpleJWT](https://django-rest-framework-simplejwt.readthedocs.io/)

You can install Python, Django, and PostgreSQL following their respective documentation.

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/sachintom999/django-backend-assignment
   ```

2. Navigate to the project directory:

   ```bash
   cd BackendAssignment
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

The project follows a standard Django project structure, including:

- `BackendAssignment/`: The main Django project folder.
- `api/`: The Django app for implementing API endpoints.
- `manage.py`: Django project management script.
- `README.md`: This README file.

## Usage

### User Registration

To register a new user, use the following endpoint:

```
POST /api/auth/register/
```

Provide the required user information (username and password ) in the request body to create a new user account.

### Authentication

Authentication is implemented using JWT tokens. To obtain an authentication token, use the following endpoint:

```
POST /api/auth/login/
```

Provide your username and password in the request body, and the server will respond with an access token, which you should include in the `Authorization` header for authenticated requests.

### Creating Posts

Authenticated users can create new posts using the following endpoint:

```
POST /api/posts/create/
```

Provide the necessary post details (title, content, etc.) in the request body along with the JWT access token in the `Authorization` header.

## Configuration

Configuration settings are stored in the Django project's settings file (`settings.py`). You can customize settings such as database configurations, JWT token settings, and more as needed.

## Database Setup

This project uses PostgreSQL as the database system. Make sure you have PostgreSQL installed and configured. Create a `.env` file using `.env.example` and add your database details

## License

This project is licensed under the [MIT License](LICENSE).
