from database.models import engine, Base, SessionLocal, Event, Course
from datetime import datetime, timedelta

def setup_database():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    
    # Check if we already have data
    if session.query(Event).first() is None:
        # Add a sample event
        event = Event(
            name="ACET Tech Fest 2026",
            description="Annual technical symposium for Engineering students.",
            event_date=datetime.now() + timedelta(days=5)
        )
        # Add a sample course reminder
        course = Course(
            name="Data Science IoT",
            reminder="Submit your final project prototype by Friday.",
            due_date=datetime.now() + timedelta(days=2)
        )
        session.add(event)
        session.add(course)
        session.commit()
    
    session.close()
    print("Database initialized and seeded.")
