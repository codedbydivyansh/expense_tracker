# CLI Expense Tracker

import json
from datetime import date

expenses = []

categories = ["Food", "Transport", "Entertainment", "Other"] 

def load_expenses():
    global expenses

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)

    except FileNotFoundError:
        expenses = []


def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():

    while True:
        try:
            amount = float(input("Enter amount: "))
            break

        except ValueError:
            print("Please enter a valid number.")

    while True:

        print("\nCategories:")
        print("Food")
        print("Transport")
        print("Entertainment")
        print("Other")

        category = input("Enter category: ").title()

        if category in categories:
            break

        print("Invalid category.")

    note = input("Enter note: ")

    today = str(date.today())

    expense = {
        "date": today,
        "category": category,
        "amount": amount,
        "note": note
    }

    expenses.append(expense)

    save_expenses()

    print("Expense added successfully!")


def view_expenses():

    if len(expenses) == 0:
        print("No expenses found.")
        return

    total = 0

    print("\nDate\t\tCategory\tAmount\tNote")
    print("-" * 50)

    for expense in expenses:

        print(
            f"{expense['date']}\t"
            f"{expense['category']}\t\t"
            f"{expense['amount']}\t"
            f"{expense['note']}"
        )

        total += expense["amount"]

    print("-" * 50)
    print(f"Total: {total}")


def filter_expenses():
    category = input("Enter category to filter by: ").title()

    found = False
    total = 0

    print("\nDate\t\tCategory\tAmount\tNote")
    print("-" * 50)

    for expense in expenses:
        if expense["category"] == category:
            print(
                f"{expense['date']}\t"
                f"{expense['category']}\t\t"
                f"{expense['amount']}\t"
                f"{expense['note']}"
            )

            total += expense["amount"]
            found = True

    if found:
        print("-" * 50)
        print(f"Total {category} Expenses: {total}")
    else:
        print("No expenses found in this category.")

load_expenses()

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