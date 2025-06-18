# Full Stack Take Home Assignment - Team Members App

This is a full-stack web application for managing team members. It includes:

- A **Django REST Framework** backend for API operations.
- A **Vue + Vite** frontend for the user interface.

The app allows you to list, create, edit, and delete team members. Roles (Admin / Regular) define permissions for each action.

---

## Project Structure

```
Full-stack-take-home-assignment/
├── backend/       ← Django REST API
│   └── README.md
├── frontend/      ← Vue + Vite SPA
│   └── README.md
└── README.md      ← You're here!
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YamiMateo/Full-stack-take-home-assignment.git
cd Full-stack-take-home-assignment
```

---

### 2. Start the backend

```bash
cd backend
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Backend will run at: `http://localhost:8000/`

---

### 3. Start the frontend

Open a new terminal tab:

```bash
cd frontend
npm install
npm run dev
```

Frontend will run at: `http://localhost:5173/`

---

## Features

- Single-page application (SPA) built with Vue 3.
- Django REST API.
- Create, list, update, and delete team members.
- Roles: `Admin` can delete, `Regular` cannot.
- CORS enabled for frontend/backend communication.

---

## Time Invested

- Backend: ~40 minutes
- Frontend: ~4 hours
- Documentation & polishing: ~1.5 hours

> Note: I spent more time on the frontend since this was my first time building a full SPA with Vue and Vite. It was a valuable learning experience!

---

## Notes

- No authentication included to keep the scope focused.
- Clean structure and separation of concerns.
- API and UI are decoupled for modular development.

---

Project ready for review!
