from datetime import datetime, timedelta
from models import User, Workout, Exercise, db

# seed.py


def seed_users():
    users = [
        User(username='alice', email='alice@example.com'),
        User(username='bob', email='bob@example.com'),
        User(username='charlie', email='charlie@example.com'),
    ]
    db.session.add_all(users)
    db.session.commit()
    return users

def seed_workouts(users):
    workouts = [
        Workout(user_id=users[0].id, date=datetime.now() - timedelta(days=2)),
        Workout(user_id=users[1].id, date=datetime.now() - timedelta(days=1)),
        Workout(user_id=users[2].id, date=datetime.now()),
    ]
    db.session.add_all(workouts)
    db.session.commit()
    return workouts

def seed_exercises(workouts):
    exercises = [
        Exercise(workout_id=workouts[0].id, name='Push Ups', reps=20, sets=3),
        Exercise(workout_id=workouts[1].id, name='Squats', reps=15, sets=4),
        Exercise(workout_id=workouts[2].id, name='Pull Ups', reps=10, sets=2),
    ]
    db.session.add_all(exercises)
    db.session.commit()

def run_seed():
    db.drop_all()
    db.create_all()
    users = seed_users()
    workouts = seed_workouts(users)
    seed_exercises(workouts)
    print("Database seeded successfully.")

if __name__ == "__main__":
    run_seed()