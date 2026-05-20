"""
Program Name: main.py

Author: Shrrayash Srinivasan

Purpose: Main file for the expense tracker.

Date: May 19, 2026

"""
expenses = []

while True:
    print("--------------------EXPENSE TRSCKER_________)")
    print("1. Expense")
    print("2. View Spending")

    option = input("Select your option")

    if option == "1":
        amount = input("Enter amount: $")
        category = input("enter category. ( food, travel, etc): ")
        print ("Amount:", amount, "Category:", category)
    

    elif option == "2":
        print(amount)




amount = input("Enter amount: $")

category = input("enter category. ( food, travel, etc): ")

print ("Amount:", amount, "Category:", category)


w = "hello"

x = "world"

print(w, x)



