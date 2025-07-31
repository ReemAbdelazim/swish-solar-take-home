# Soiling Loss Visualization – Full Stack App

This is a simple full stack project that simulates and displays soiling loss over time.

- The **backend** (FastAPI) generates synthetic soiling loss data for the past 30 days.
- The **frontend** (Next.js) fetches that data and displays it as a clean line chart using Chart.js.

---

## Project Structure

project-root/
│
├── backend/ # FastAPI app
│ └── main.py
│ └── requirements.txt
│
├── frontend/ # Next.js app (React + Chart.js)
│ └── README.md
│ └── src/app/page.tsx
│ └── package.json


---

## How to Run the Project Locally

### 1. Start the Backend

1. Open a terminal and go into the backend folder:
cd backend

2. Create a virtual environment (optional but recommended):
python -m venv .venv
.venv\Scripts\activate # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Run the server:
uvicorn main:app --reload

The backend should now be running at:  
`http://localhost:8000/soiling`

---

### 2. Start the Frontend

1. Open a second terminal and go into the frontend folder:
cd frontend

2. Install dependencies:
npm install

3. Start the Next.js app:
npm run dev

The frontend will be live at:  
`http://localhost:3000`

For frontend-specific info, check:  
[`frontend/README.md`](frontend/README.md)

---

## Requirements

### Backend:
- Python 3.8+
- FastAPI
- Uvicorn

Install with:
pip install -r backend/requirements.txt

### Frontend:
- Node.js (v18+)
- Uses `next`, `react`, `chart.js`, and `react-chartjs-2`

---

## What It Does

- Simulates daily soiling loss (random + increasing)
- Exposes it as a JSON API (`/soiling`)
- Displays it as a line chart (1 line, 30 points)
- Handles loading and errors gracefully