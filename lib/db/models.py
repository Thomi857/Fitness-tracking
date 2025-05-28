# lib/db/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship, validates, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    workout_sessions = relationship("WorkoutSession", back_populates="user", cascade="all, delete")
    health_records = relationship("HealthRecord", back_populates="user", cascade="all, delete")

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"

    @validates('email')
    def validate_email(self, key, address):
        assert "@" in address, "Invalid email format."
        return address

    @validates('name')
    def validate_name(self, key, value):
        assert len(value.strip()) > 0, "Name cannot be empty."
        return value

class WorkoutSession(Base):
    __tablename__ = 'workout_sessions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(Date, nullable=False)
    type = Column(String, nullable=False)
    duration_minutes = Column(Integer)

    user = relationship("User", back_populates="workout_sessions")

    def __repr__(self):
        return f"WorkoutSession(id={self.id}, type='{self.type}', date={self.date})"

    @validates('duration_minutes')
    def validate_duration(self, key, value):
        assert value > 0, "Duration must be greater than 0."
        return value

class HealthRecord(Base):
    __tablename__ = 'health_records'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(Date, nullable=False)
    weight_kg = Column(Float)
    blood_pressure = Column(String)
    heart_rate = Column(Integer)
    sleep_hours = Column(Float)

    user = relationship("User", back_populates="health_records")

    def __repr__(self):
        return f"HealthRecord(id={self.id}, date={self.date}, weight={self.weight_kg}kg)"
