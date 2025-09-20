"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    # Intellectual Activities
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Science Olympiad": {
        "description": "Prepare for competitive science events and experiments",
        "schedule": "Saturdays, 9:00 AM - 11:00 AM",
        "max_participants": 15,
        "participants": ["alice@mergington.edu", "bob@mergington.edu"]
    },
    "Debate Team": {
        "description": "Develop public speaking and argumentation skills through competitive debates",
        "schedule": "Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["carlos@mergington.edu"]
    },
    "Math Club": {
        "description": "Explore advanced mathematics concepts and participate in competitions",
        "schedule": "Thursdays, 3:45 PM - 5:15 PM",
        "max_participants": 14,
        "participants": ["jennifer@mergington.edu", "kevin@mergington.edu"]
    },
    "Robotics Team": {
        "description": "Build and program robots for competitive robotics challenges",
        "schedule": "Saturdays, 2:00 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["ryan@mergington.edu"]
    },
    
    # Sports Activities
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Competitive basketball training and inter-school tournaments",
        "schedule": "Mondays and Wednesdays, 4:00 PM - 6:00 PM",
        "max_participants": 15,
        "participants": ["marcus@mergington.edu", "sarah@mergington.edu"]
    },
    "Swimming Club": {
        "description": "Swimming techniques, water safety, and competitive swimming",
        "schedule": "Tuesdays and Thursdays, 6:00 AM - 7:30 AM",
        "max_participants": 20,
        "participants": ["alex@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Competitive soccer training and inter-school matches",
        "schedule": "Tuesdays and Fridays, 4:00 PM - 6:00 PM",
        "max_participants": 22,
        "participants": ["diego@mergington.edu", "maria@mergington.edu"]
    },
    "Track and Field": {
        "description": "Running, jumping, and throwing events for athletic development",
        "schedule": "Mondays and Thursdays, 3:30 PM - 5:30 PM",
        "max_participants": 25,
        "participants": ["james@mergington.edu", "natalie@mergington.edu", "victor@mergington.edu"]
    },
    
    # Artistic Activities
    "Drama Club": {
        "description": "Acting, scriptwriting, and theatrical productions",
        "schedule": "Fridays, 4:00 PM - 6:00 PM",
        "max_participants": 25,
        "participants": ["elena@mergington.edu", "david@mergington.edu", "lisa@mergington.edu"]
    },
    "Art Studio": {
        "description": "Painting, drawing, sculpture and various visual arts techniques",
        "schedule": "Saturdays, 1:00 PM - 4:00 PM",
        "max_participants": 16,
        "participants": ["maya@mergington.edu", "jackson@mergington.edu"]
    },
    "Music Band": {
        "description": "Learn instruments and perform in school concerts and events",
        "schedule": "Wednesdays and Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 30,
        "participants": ["sophia@mergington.edu", "lucas@mergington.edu", "isabella@mergington.edu"]
    },
    "Photography Club": {
        "description": "Learn photography techniques, digital editing, and showcase artistic vision",
        "schedule": "Sundays, 10:00 AM - 1:00 PM",
        "max_participants": 18,
        "participants": ["rachel@mergington.edu", "ethan@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up")

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
