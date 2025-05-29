# from datetime import date
# from lib.db.models import Base, User, WorkoutSession, HealthRecord
# from lib.db.database import session, engine

# # Create tables if they don't exist
# Base.metadata.create_all(engine)

# # Check if user already exists to prevent duplicates
# existing_user = session.query(User).filter_by(email="alicesmith7@gmail.com").first()

# if not existing_user:
#     # Create test user
#     user1 = User(name="Alice Smith", email="alicesmith7@gmail.com")

#     # Create workouts
#     workout1 = WorkoutSession(
#         user=user1,
#         date=date(2024, 6, 1),
#         type="Cardio",
#         duration_minutes=45
#     )

#     workout2 = WorkoutSession(
#         user=user1,
#         date=date(2024, 6, 3),
#         type="Strength",
#         duration_minutes=30
#     )

#     # Create health records
#     record1 = HealthRecord(
#         user=user1,
#         date=date(2024, 6, 1),
#         weight_kg=65.5,
#         blood_pressure="120/80",
#         heart_rate=72,
#         sleep_hours=7.5
#     )

#     record2 = HealthRecord(
#         user=user1,
#         date=date(2024, 6, 3),
#         weight_kg=65.0,
#         blood_pressure="118/79",
#         heart_rate=70,
#         sleep_hours=8.0
#     )

#     # Add and commit
#     session.add_all([user1, workout1, workout2, record1, record2])
#     session.commit()
#     print(" Database seeded with test data.")
# else:
#     print("ℹ  Test user already exists. Skipping seeding.")


from datetime import date
from lib.db.models import Base, User, WorkoutSession, HealthRecord
from lib.db.database import session

# Create user and embed workouts directly
new_user = User(
    name="John Doe",
    email="johndoe@example.com",
    workout_sessions=[
        WorkoutSession(
            date=date(2024, 6, 10),
            type="Cycling",
            duration_minutes=60
        ),
        WorkoutSession(
            date=date(2024, 6, 12),
            type="Weight Training",
            duration_minutes=45
        )
    ]
)

new_user = User(
    name="Jane Doe",
    email="janedoe@example.com",
    workout_sessions=[
        WorkoutSession(date=date(2024, 6, 11), type="Pilates", duration_minutes=40)
    ],
    health_records=[
        HealthRecord(date=date(2024, 6, 11), weight_kg=64.0, blood_pressure="122/78", heart_rate=74, sleep_hours=8)
    ]
)

# Add to DB
session.add(new_user)
session.commit()

print(f" Created user {new_user.name} with {len(new_user.workout_sessions)} workouts.")
