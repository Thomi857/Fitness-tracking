# lib/db/seed.py
from lib.db.models import Base, User, WorkoutSession, HealthRecord
from lib.db.database import session
from datetime import date

# Create test user
user1 = User(name="Alice Smith", email="alice@example.com")

# Create workouts
workout1 = WorkoutSession(
    user=user1,
    date=date(2024, 6, 1),
    type="Cardio",
    duration_minutes=45
)

workout2 = WorkoutSession(
    user=user1,
    date=date(2024, 6, 3),
    type="Strength",
    duration_minutes=30
)

# Create health records
record1 = HealthRecord(
    user=user1,
    date=date(2024, 6, 1),
    weight_kg=65.5,
    blood_pressure="120/80",
    heart_rate=72,
    sleep_hours=7.5
)

record2 = HealthRecord(
    user=user1,
    date=date(2024, 6, 3),
    weight_kg=65.0,
    blood_pressure="118/79",
    heart_rate=70,
    sleep_hours=8.0
)

# Add and commit
session.add_all([user1, workout1, workout2, record1, record2])
session.commit()
print("Database seeded with test data!")
