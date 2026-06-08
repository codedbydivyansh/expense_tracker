# CLI Expense Tracker

def load_expenses():
    pass


def save_expenses():
    pass


def add_expense():
    pass


def view_expenses():
    pass


def filter_expenses():
    pass


while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Filter By Category")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        filter_expenses()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")