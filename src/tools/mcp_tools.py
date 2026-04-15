import os
import requests
from datetime import datetime, timedelta
from database.models import SessionLocal, Event, Course

def get_campus_events():
    session = SessionLocal()
    events = session.query(Event).all()
    session.close()
    return [{"name": e.name, "date": e.event_date.isoformat()} for e in events]

def get_course_reminders(program):
    session = SessionLocal()
    courses = session.query(Course).all()
    session.close()
    return [{"name": c.name, "reminder": c.reminder} for c in courses]

def get_weather_forecast(location):
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric"
    try:
        r = requests.get(url, timeout=10)
        return r.json()['list'][0] if r.status_code == 200 else "Weather unavailable"
    except:
        return "Weather unavailable"
