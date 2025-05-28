# lib/cli.py
from lib.db.database import session
from lib.db.models import User, WorkoutSession, HealthRecord
from lib.helpers import get_nonempty_input, get_int_input

def main_menu():
    while True:
        print("\n=== Fitness Tracker CLI ===")
        print("1. View all users")
        print("2. Add user")
        print("3. Delete user")
        print("4. View workouts by user ID")
        print("5. View health records by user ID")
        print("6. Exit")
        choice = input("> ")

        if choice == "1":
            for user in session.query(User).all():
                print(user)
        elif choice == "2":
            name = get_nonempty_input("Name: ")
            email = get_nonempty_input("Email: ")
            user = User(name=name, email=email)
            session.add(user)
            session.commit()
            print(f"Added user {user.name}")
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
                for w in user.workout_sessions:
                    print(w)
            else:
                print("User not found.")
        elif choice == "5":
            uid = get_int_input("User ID: ")
            user = session.get(User, uid)
            if user:
                for h in user.health_records:
                    print(h)
            else:
                print("User not found.")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main_menu()
