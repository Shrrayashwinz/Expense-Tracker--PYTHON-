"""
Program Name: main.py

Author: Shrrayash Srinivasan

Purpose: Main file for the expense tracker.

Date: May 20, 2026

"""
#import json
   
#import os

def load_data():
    pass

#----------------FUNCTIONS==========================

def add_expense():
    try: 
        amount = input("Enter amount: $")
    except ValueError:
        print("!!ERROR!!")
        return
    category = input("enter category. ( food, travel, etc): ")

    expenses = ("Amount:", amount, "Category:", category)

    expenses.append(expenses)



def view_expense():
    if expenses is None:
        print("No expenses to see here!")
        return
    
    else:
        print("\n----------Expenses----------")
        




def total_spending():
    pass

expenses = []


amount = input("Enter amount: $")

category = input("enter category. ( food, travel, etc): ")

print ("Amount:", amount, "Category:", category)


w = "hello"

x = "world"

print(w, x)

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

    elif option == "2":
        print(category, amount)
    
    elif option == "3":
        total_spending = amount
        print(amount)

    elif option == "4":
        print("Have an awesome day!")
        break
    
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    main()



