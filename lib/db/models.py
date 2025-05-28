from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()  # ✅ Only one call here

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    age = Column(Integer)
    weight = Column(Float)
    height = Column(Float)

    workouts = relationship('Workout', back_populates='user')

class Workout(Base):
    __tablename__ = 'workouts'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(Date, nullable=False)
    workout_type = Column(String, nullable=False)
    duration_minutes = Column(Integer)
    calories_burned = Column(Float)

    user = relationship('User', back_populates='workouts')
