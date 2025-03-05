"""
Name: grocery_app.py
Author: Andrew Peterson
Date: 02/05/2024
Purpose: Create an application for a grocery database
"""

import tabulate
import groccery_list
import shopping_list

MENU_PROMPT = """------ Groccery Inventory App    ------
(1) Add Groccery
(2) Display All Groccery
(3) Update Groccery
(4) Delete a Groccery
(5) Exit
Your Selection: """

THRESHOLD = 1

def main():
    groccery_list.create_table()
    menu()

def menu():
    while True:
        user_input = input(MENU_PROMPT)

        if user_input == "1":

            groccery_name = input("Enter Groccery Name: ")
            groccery_type = input("Enter Groccery Type: ")
            groccery_price = float(input("Enter Groccery Price: "))
            groccery_quantity = int(input("Enter Groccery Quantity: "))

            groccery_list.add_groccery(
                groccery_name,
                groccery_type,
                groccery_price,
                groccery_quantity
            )

            display_all_groccerys()

        elif user_input == "2":
            display_all_groccerys()

        elif user_input == "3":
            display_all_groccerys()

            groccery_id = int(input("Enter Groccery ID: "))
            groccery_quantity = int(input("Enter Groccery Quantity: "))

            groccery_list.update_groccery(groccery_id, groccery_quantity)

            display_all_groccerys()
            
        elif user_input == "4":
            display_all_groccerys()

            groccery_id = int(input("Enter Groccery ID: "))

            groccery_list.delete_groccery(groccery_id)

            display_all_groccerys()
        elif user_input == "5":
            break
        else:
            print("Invalid input, please try again!")

    check_inventory()

def display_all_groccerys():
    groccerys = groccery_list.fetch_all_groccerys()

    list = tabulate.tabulate(
        groccerys,
        headers=["Groccery ID","Groccery Name","Groccery Type","Groccery Price","Groccery Quantity"],
        tablefmt="psql"
    )

    print(list)

def check_inventory():
    grocceries = groccery_list.fetch_all_groccerys()
    sh_list = shopping_list.fetch_all_groccerys()
    shopping_list.create_table()
    print("Shopping List")
    updated = False
    for item in grocceries:
        if item[4] <= THRESHOLD:
            print(f"running low on {item[1]}'s")
            print(f"Adding {item[1]}'s to the shopping list")
            groccery_name = item[1]
            groccery_type = item[2]
            groccery_price = item[3]
            groccery_quantity = THRESHOLD - item[4]

            for groc in sh_list:
                if groccery_name == groc[1]:
                    shopping_list.update_groccery(groc[0], groccery_quantity)
                    if groccery_quantity == 0:
                        shopping_list.delete_groccery(groc[0])
                    updated = True
                    break
            if updated == False:
                shopping_list.add_groccery(
                    groccery_name,
                    groccery_type,
                    groccery_price,
                    groccery_quantity
                )

    list = tabulate.tabulate(
        sh_list,
        headers=["Groccery ID","Groccery Name","Groccery Type","Groccery Price","Groccery Quantity"],
        tablefmt="psql"
    )

    print(list)

main()
