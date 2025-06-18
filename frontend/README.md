# Frontend - Team Members App

This is the **frontend** for the **Team Members App**, built using **Vue 3** and **Vite**. It is a single-page application (SPA) that connects to the Django REST API to manage team members.

---

## Requirements

- Node.js 18+
- npm or yarn

---

## Installation

1. Navigate to the frontend directory:

```bash
cd frontend
```

2. Install dependencies:

```bash
npm install
# or
yarn install
```

3. Start the development server:

```bash
npm run dev
# or
yarn dev
```

The app will run at: `http://localhost:5173`

> Make sure the backend server is running at `http://localhost:8000` so the API can be consumed correctly.

---

## Features

- **List** all team members.
- **Add** a new member with first name, last name, email, phone, and role.
- **Edit** existing member information and change their role.
- **Delete** members from the list.
- Role-based actions:
  - `Admin`: can delete members.
  - `Regular`: cannot delete members.

---

## API Connection

This project uses **Axios / Fetch** to make requests to the backend API hosted at:

```
http://localhost:8000/api/team-members/
```

CORS is enabled on the backend to allow communication.

## Testing

No automated tests have been implemented.  
Future improvements could include unit testing using **Jest** or **Vue 3 Testing Library**.

---

Ready to use!
