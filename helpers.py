# To-do list application
def to_do_list():
  tasks = []
  while True:
    print("\n1.Show\n2.Add\n3.Remove\n4.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
      print("Tasks:" if tasks else "No tasks")
      for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    elif choice == "2":
      task = input("Enter the task: ")
      tasks.append(task)
    elif choice == "3":
      if tasks:
        print("Tasks:" if tasks else "No tasks")
        for i, task in enumerate(tasks, 1):
          print(f"{i}. {task}")
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
          tasks.pop(index)
        else:
          print("Invalid task number.")
      else:
        print("No tasks to remove.")
    elif choice == "4":
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")
# Study planner application
def study_planner():
  subjects = {}
  while True:
    print("\n1.Show\n2.Add\n3.Remove\n4.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
      print("Subjects:" if subjects else "No subjects")
      for subject, hours in subjects.items():
        print(f"{subject}: {hours} hours")
    elif choice == "2":
      subject = input("Enter the subject: ")
      hours = float(input("Enter study hours: "))
      subjects[subject] = hours
    elif choice == "3":
      if subjects:
        print("Subjects:" if subjects else "No subjects")
        for subject in subjects.keys():
          print(subject)
        subject_to_remove = input("Enter the subject to remove: ")
        if subject_to_remove in subjects:
          del subjects[subject_to_remove]
        else:
          print("Subject not found.")
      else:
        print("No subjects to remove.")
    elif choice == "4":
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")
# Budget tracker application
def budget_tracker():
  budget = int(input("Enter your budget: "))
  expenses = []
  income = []
  while True:
    print("\n1.Show\n2.Add Expense\n3.Add Income\n4.Set Budget\n5.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
      print(f"Budget: R{budget}")
      print("Expenses:" if expenses else "No expenses")
      for expense in expenses:
        print(f"- R{expense}")
      print("Income:" if income else "No income")
      for amount in income:
        print(f"- R{amount}")
    elif choice == "2":
      expense = float(input("Enter the expense amount: "))
      expenses.append(expense)
    elif choice == "3":
      amount = float(input("Enter the income amount: "))
      income.append(amount)
    elif choice == "4":
      budget = int(input("Enter the budget amount: "))
    elif choice == "5":
      print("Exiting...")
      break
    else:
      print("Invalid choice. Please try again.")  