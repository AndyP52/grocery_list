"""
Name: grocery_app.py
Author: Andrew Peterson
Date: 02/05/2024
Purpose: Create an application for a grocery database
"""

import tabulate
import grocery_list

MENU_PROMPT = """------ Football Library App    ------
(1) Add Grocery
(2) Display All Grocery
(3) Delete a Grocery
(4) Exit
Your Selection: """

def main():
    grocery_list.create_table()
    menu()

def menu():
    while True:
        user_input = input(MENU_PROMPT)

        if user_input == "1":

            grocery_name = input("Enter Grocery Name: ")
            grocery_type = input("Enter Grocery Type: ")
            grocery_price = float(input("Enter Grocery Price: "))
            grocery_quantity = int(input("Enter Grocery Quantity: "))

            grocery_list.add_grocery(
                grocery_name,
                grocery_type,
                grocery_price,
                grocery_quantity

            )

            display_all_grocerys()

        elif user_input == "2":
            display_all_grocerys()
            
        elif user_input == "3":
            display_all_grocerys()

            grocery_id = int(input("Enter Grocery ID: "))

            grocery_list.delete_grocery(grocery_id)

            display_all_grocerys()
        elif user_input == "4":
            break
        else:
            print("Invalid input, please try again!")

def display_all_grocerys():
    grocerys = grocery_list.fetch_all_grocerys()

    list = tabulate.tabulate(
        grocerys,
        headers=["Grocery ID","Grocery Name","Grocery Type","Groccery Price","Grocery Quantity"],
        tablefmt="psql"
    )

    print(list)

main()
