"""
Program Name: main.py
Author: Shrrayash Srinivasan
Purpose: Main file for the expense tracker.
Date: May 20, 2026
"""

import json
import os

DATA_FILE = "data.json"

# ----------- Load and Save ------------------------------

def load_data():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_data(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)


# ---------------- FUNCTIONS --------------------------

def add_expenses(expenses):
    try:
        amount = float(input("Enter amount: $"))
    except ValueError:
        print("!! ERROR: Amount must be a number !!")
        return

    category = input("Enter category (food, travel, etc): ").strip().lower()

    # Store as dictionary (IMPORTANT FIX)
    expense = {"amount": amount, "category": category}
    expenses.append(expense)

    save_data(expenses)
    print("Your expense has been added!")


def view_expenses(expenses):
    if not expenses:
        print("No expenses to see here!")
        return

    print("\n---------- Expenses ----------")
    for e in expenses:
        print(f"${e['amount']} - {e['category']}")


def total_spending(expenses):
    total = sum(e["amount"] for e in expenses)
    print(f"Total Spending: ${total}")


def category_breakdown(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    breakdown = {}

    for e in expenses:
        cat = e["category"]
        breakdown[cat] = breakdown.get(cat, 0) + e["amount"]

    print("\n--- Category Breakdown ---")
    for cat, amt in breakdown.items():
        print(f"{cat.capitalize()}: ${amt}")


# -------------------------------------
# main function
# -------------------------------------

def main():

    expenses = load_data()

    while True:
        print("\nWelcome to the Expense Tracker")
        print("1. Add expense")
        print("2. View expenses")
        print("3. View total spending")
        print("4. Category breakdown")
        print("5. Exit")

        option = input("Select option: ")

        if option == "1":
            add_expenses(expenses)

        elif option == "2":
            view_expenses(expenses)

        elif option == "3":
            total_spending(expenses)

        elif option == "4":
            category_breakdown(expenses)

        elif option == "5":
            print("Have an awesome day!")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()




