import os
from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

load_dotenv()
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    chat_id = Column(BigInteger, unique=True, nullable=False)
    college = Column(String, nullable=False)
    program = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    event_date = Column(DateTime, nullable=False)

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    reminder = Column(String, nullable=False)
    due_date = Column(DateTime, nullable=False)

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:////app/data/newsletter.db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
