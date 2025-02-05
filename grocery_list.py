"""
Name: grocery_list.py
Author: Andrew Peterson
Date: 02/05/2024
Purpose: Create a grocery database
"""


# import libary
import sqlite3

DATABASE = 'grocery_list.db'

CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS tbl_grocery (
        grc_id      INTEGER PRIMARY KEY,
        grc_name   TEXT,
        grc_type    TEXT,
        grc_price     REAL,
        grc_quantity     INT
    );
    """
INSERT_INTO_TABLE = """
    INSERT INTO tbl_grocery (
    grc_name,
    grc_type,
    grc_price,
    grc_quantity
    ) VALUES (?, ?, ?, ?);
"""

FETCH_ALL_GROCERYS = "Select * From tbl_grocery;"

DELETE_GROCERY = "DELETE FROM tbl_grocery WHERE grc_id = ?"

# create the table
def create_table():
    with sqlite3.connect(DATABASE) as connection:
        # create a cursor object
        cursor = connection.cursor()

        # execute the scipt against database
        cursor.execute(CREATE_TABLE)

def add_grocery(grc_name, grc_type, grc_price, grc_quantity):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()

        cursor.execute(
            INSERT_INTO_TABLE,
            (grc_name, grc_type, grc_price, grc_quantity)
        )

def fetch_all_grocerys():
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()

        grocerys = cursor.execute(FETCH_ALL_GROCERYS).fetchall()

        return grocerys
    
def delete_grocery(grc_id):
    with sqlite3.connect(DATABASE) as connection:

        cursor = connection.cursor()

        cursor.execute(DELETE_GROCERY, (grc_id, ))

