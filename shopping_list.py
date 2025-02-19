"""
Name: grocery_list.py
Author: Andrew Peterson
Date: 02/05/2024
Purpose: Create a grocery database
"""


# import libary
import sqlite3

DATABASE = 'shopping_list.db'

CREATE_TABLE = """
    CREATE TABLE IF NOT EXISTS tbl_shopping (
        grc_id      INTEGER PRIMARY KEY,
        grc_name   TEXT,
        grc_type    TEXT,
        grc_price     REAL,
        grc_quantity     INT
    );
    """
INSERT_INTO_TABLE = """
    INSERT INTO tbl_shopping (
    grc_name,
    grc_type,
    grc_price,
    grc_quantity
    ) VALUES (?, ?, ?, ?);
"""

FETCH_ALL_GROCCERYS = "Select * From tbl_shopping;"

DELETE_GROCCERY = "DELETE FROM tbl_shopping WHERE grc_id = ?"

# create the table
def create_table():
    with sqlite3.connect(DATABASE) as connection:
        # create a cursor object
        cursor = connection.cursor()

        # execute the scipt against database
        cursor.execute(CREATE_TABLE)

def add_groccery(grc_name, grc_type, grc_price, grc_quantity):
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()

        cursor.execute(
            INSERT_INTO_TABLE,
            (grc_name, grc_type, grc_price, grc_quantity)
        )

def fetch_all_groccerys():
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()

        groccerys = cursor.execute(FETCH_ALL_GROCCERYS).fetchall()

        return groccerys
    
def delete_groccery(grc_id):
    with sqlite3.connect(DATABASE) as connection:

        cursor = connection.cursor()

        cursor.execute(DELETE_GROCCERY, (grc_id, ))
