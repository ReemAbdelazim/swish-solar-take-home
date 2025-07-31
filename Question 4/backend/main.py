"""
FastAPI backend that simulates soiling loss percentage data over the past 30 days.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timedelta
import random

app = FastAPI()

# Allow frontend access (e.g. http://localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/soiling")
def get_soiling_data():
    """
    Return simulated soiling loss estimates over the last 30 days.
    
    Returns:
        list of dicts: Each entry contains a date and its corresponding soiling_loss_percent.
    """
    today = datetime.today()
    data = [
        {
            "date": (today - timedelta(days=i)).strftime("%Y-%m-%d"),
            "soiling_loss_percent": round(5 + random.uniform(-1, 1) + 0.2 * i, 2)
        }
        for i in range(30)
    ]
    return list(reversed(data))
