"""
Program Name: main.py

Author: Shrrayash Srinivasan

Purpose: Main file for the expense tracker.

Date: May 20, 2026

"""
import json
   
import os

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
#----------------FUNCTIONS==========================

def add_expenses(expenses):
    try: 
        amount = input("Enter amount: $")
    except ValueError:
        print("!!ERROR!!")
        return
    category = input("enter category. ( food, travel, etc): ")

    expenses = ("Amount:", amount, "Category:", category)

    expenses.append(expenses)

    save_data(expenses)
    print("Your expense has been added!")



def view_expenses(expenses):
    if expenses is None:
        print("No expenses to see here!")
        return
    

    print("\n----------Expenses----------")
    for e in expenses:
        print(f"${e['amount']} - {e['category']}")
        




def total_spending(expenses):
    total = sum(e["amount"] for e in expenses)
    print("Total Spending amounts to", total)

def category_breakdown(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    
    breakdown = []

    for e in expenses:
        cat = e["category"]
        breakdown[cat] = breakdown.get(cat, 0) + e["amount"]

    print("\n--- Category Breakdown ---")
    for cat, amt in breakdown.items():
        print(f"{cat.capitalize()}: ${amt}")



#-------------------------------------
# main function
#-------------------------------------

def main():
 
  expenses = load_data()

  while True:
    print("\nWelcome to the Expense tracker")
    print("1. add expense")
    print("2. view expenses")
    print("3. view total spending")
    print("4. Exit")

    option = input("Select option: ")


    if option == "1":
        amount = float(input("Enter amount: $"))
        category = input("enter category. ( food, travel, etc): ")

        print ("Amount:", amount, "Category:", category)

        add_expenses(expenses)

    elif option == "2":
        print(category, amount)
        view_expenses(expenses)
    
    elif option == "3":
        total_spending = amount
        print(amount)
        total_spending(expenses)

    elif option == "4":
        print("Have an awesome day!")
        break
    
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    main()



