from lib.db.database import session
from lib.db.models import User, WorkoutSession, HealthRecord
from lib.helpers import get_nonempty_input, get_int_input
from datetime import datetime

def main_menu():
    while True:
        print("\n=== Fitness Tracker CLI ===")
        print("1. View all users")
        print("2. Add user")
        print("3. Delete user")
        print("4. View workouts by user ID")
        print("5. View health records by user ID")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            for user in session.query(User).all():
                print(user)

        elif choice == "2":
            name = get_nonempty_input("Name: ")
            email = get_nonempty_input("Email: ")
            user = User(name=name, email=email)

            workouts = []
            while True:
                add_workout = input("Add a workout for this user? (y/n): ").strip().lower()
                if add_workout == 'y':
                    try:
                        w_date_str = get_nonempty_input("Workout date (YYYY-MM-DD): ")
                        w_date = datetime.strptime(w_date_str, "%Y-%m-%d").date()
                        w_type = get_nonempty_input("Workout type (e.g., Cardio, Strength): ")
                        muscle_group = None
                        if w_type.lower() == "strength":
                            print("Select the muscle group to target:")
                            muscle_groups = ["Chest", "Back", "Legs", "Arms", "Shoulders", "Core", "Other"]
                            for idx, group in enumerate(muscle_groups, 1):
                                print(f"{idx}. {group}")
                            while True:
                                try:
                                    mg_choice = int(input("Enter the number for the muscle group: "))
                                    if 1 <= mg_choice <= len(muscle_groups):
                                        muscle_group = muscle_groups[mg_choice - 1]
                                        break
                                    else:
                                        print("Invalid selection. Please choose a valid number.")
                                except ValueError:
                                    print("Please enter a number.")
                            print(f"Targeted muscle group: {muscle_group}")
                        w_duration = get_int_input("Duration in minutes: ")

                        workout = WorkoutSession(
                            date=w_date,
                            type=w_type,
                            duration_minutes=w_duration,
                            muscle_group=muscle_group  # Make sure your WorkoutSession model has this column
                        )
                        w_duration = get_int_input("Duration in minutes: ")

                        workout = WorkoutSession(
                            date=w_date,
                            type=w_type,
                            duration_minutes=w_duration
                        )
                        workouts.append(workout)
                    except ValueError:
                        print(" Invalid date format. Use YYYY-MM-DD.")
                    except Exception as e:
                        print(f" Error creating workout: {e}")
                elif add_workout == 'n':
                    break
                else:
                    print("Please enter 'y' or 'n'.")

            user.workout_sessions = workouts
            session.add(user)
            session.commit()
            print(f" Added user {user.name} with {len(workouts)} workout(s).")

        elif choice == "3":
            user_id = get_int_input("User ID to delete: ")
            user = session.get(User, user_id)
            if user:
                session.delete(user)
                session.commit()
                print("User deleted.")
            else:
                print("User not found.")

        elif choice == "4":
            uid = get_int_input("User ID: ")
            user = session.get(User, uid)
            if user:
                if user.workout_sessions:
                    print(f"\n=== Workouts for {user.name} ===")
                    for w in user.workout_sessions:
                        print(f"- {w.date}: {w.type} ({w.duration_minutes} mins)")
                else:
                    print(f"No workouts found for {user.name}.")
            else:
                print("User not found.")

        elif choice == "5":
            uid = get_int_input("User ID: ")
            user = session.get(User, uid)
            if user:
                if user.health_records:
                    print(f"\n=== Health Records for {user.name} ===")
                    for h in user.health_records:
                        print(h)
                else:
                    print(f"No health records found for {user.name}.")
            else:
                print("User not found.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main_menu()
