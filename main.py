# Main Menu
import helpers

def main_menu():
    print("Welcome to the Main Menu!")
    while True:
        print("\n1.To-Do List")
        print("2. Study Planner")
        print("3. Budget Tracker")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            helpers.to_do_list()
        elif choice == "2":
            helpers.study_planner()
        elif choice == "3":
            helpers.budget_tracker()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main_menu()