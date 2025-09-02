# MindSync

A health application with FastAPI backend and Vue.js frontend.

## Technologies Needed

- **Python 3.8+** with pip
- **Node.js 16+** with npm
- **Git**

## How to Replicate on Your Machine

1. **Clone and setup:**
```bash
git clone <repository-url>
cd MindSync
```

2. **Start backend:**
```bash
cd server
pip install -r requirements.txt
python main.py
```

3. **Start frontend (new terminal):**
```bash
cd client
npm install
npm run dev
```

4. **Access:**
- Backend: http://localhost:8000
- Frontend: http://localhost:3000

## Backend

FastAPI server with SQLAlchemy ORM. Handles user management with SQLite database.

## Frontend

Vue.js 3 app with Vite. Simple testing interface for user operations.
