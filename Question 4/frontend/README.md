# Frontend – Soiling Loss Dashboard

This is the frontend for the Soiling Loss project. It fetches data from the backend and shows a simple line chart of soiling loss over the past 30 days.

### What it's built with:
- Next.js (App Router)
- React
- Chart.js (via react-chartjs-2)

---

### How to run it:

1. Make sure the backend is running at:  
   `http://localhost:8000/soiling`

2. Go into the frontend folder:

cd frontend

3. Install the dependencies:

npm install

4. Start the app:

npm run dev

5. Open your browser:  
   [http://localhost:3000](http://localhost:3000)

---

### Notes:
- If you see a CORS error, check that CORS is enabled in the backend.
- If it says "Failed to load data", your backend might not be running.
- Check the main read me for overall set up.