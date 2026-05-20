"""
Program Name: main.py

Author: Shrrayash Srinivasan

Purpose: Main file for the expense tracker.

Date: May 19, 2026

"""

expenses = []


amount = input("Enter amount: $")

category = input("enter category. ( food, travel, etc): ")

print ("Amount:", amount, "Category:", category)


w = "hello"

x = "world"

print(w, x)

while True:
    print("Welcome to the Expense tracker")
    print("1. add expense")
    print("2. view expenses")
    print("3. view total spending")
    print("4. Exit")

    option = int(input("Select option: "))


    if option == "1":
        amount = float(input("Enter amount:"))
        category = input("enter category. ( food, travel, etc): ")

        print ("Amount:", amount, "Category:", category)

    elif option == "2":
        print(category, amount)
    
    elif option == "3":
        total_spending = amount
        print(amount)

    elif option == "4":
        print("Have an awesome day!")
    
    else:
        print("Invalid Choice")



