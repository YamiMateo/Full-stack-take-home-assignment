# Backend - Team Members App

This is the **backend** for the **Team Members App**, developed as part of the *Full Stack Take Home Assignment*. It is built with **Django 5.2.1** and **Django REST Framework**, providing a RESTful API to manage team member data.

---

## Requirements

- Python 3.10+
- virtualenv (optional but recommended)
- SQLite (default database)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YamiMateo/Full-stack-take-home-assignment.git
cd Full-stack-take-home-assignment/backend
```

2. Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate  
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

The server will be running at: `http://127.0.0.1:8000/`

---

## Available Endpoints

| Method | Endpoint             | Description           |
|--------|----------------------|-----------------------|
| GET    | /api/team-members/        | List all team members |
| POST   | /api/team-members/        | Create a new member   |
| GET    | /api/team-members/<id>/   | Retrieve a member     |
| PUT    | /api/team-members/<id>/   | Update a member       |
| DELETE | /api/team-members/<id>/   | Delete a member       |

---

## CORS

CORS is enabled for all origins (`CORS_ALLOW_ALL_ORIGINS = True`) to allow frontend apps (such as the one running at `http://localhost:5173`) to consume the API without restrictions.

---

## Dependencies

To generate the `requirements.txt` file, the following command was used:

```bash
pip freeze > requirements.txt
```

---

