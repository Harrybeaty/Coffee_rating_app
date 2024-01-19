import sqlite3

CREATE_COFFEE_TABLE = "CREATE TABLE IF NOT EXISTS coffee (id INTEGER PRIMARY KEY, name TEXT, method TEXT, strength INTEGER, mum_rating INTEGER, harry_rating INTEGER);"
INSERT_COFFEE = "INSERT INTO coffee (name, method, strength, mum_rating, harry_rating) VALUES (?, ?, ?, ?, ?);" 
GET_ALL_COFFEE = "SELECT * FROM coffee"
GET_COFFEE_BY_NAME = "SELECT * FROM coffee WHERE name = ?;"
GET_BEST_METHOD_FOR_COFFEE = """
SELECT * FROM coffee
WHERE name = ?
ORDER BY harry_rating DESC
LIMIT 1;"""
GET_TOP_10_RATINGS = "SELECT * FROM coffee ORDER BY harry_rating DESC LIMIT 10;"

# Connects python with sql so we can use this to write sql code.
def connect():
    return sqlite3.connect("data.db")                       

# Open connection and create table with SQL.
def create_tables(connection):
    with connection:
        connection.execute(CREATE_COFFEE_TABLE)

def add_bean(connection, name, method, strength, harry_rating, mum_rating):
    with connection:
        connection.execute(INSERT_COFFEE, (name, method, strength, harry_rating, mum_rating))

def get_all_coffee(connection):
    with connection:
        return connection.execute(GET_ALL_COFFEE).fetchall()                 # As it is getting data we need to return it from the function. it returns as a list.

def get_coffee_by_name(connection, name):
    with connection:
        return connection.execute(GET_COFFEE_BY_NAME, (name,)).fetchall()
    
def get_best_method_for_coffee(connection, name):
    with connection:
        return connection.execute(GET_BEST_METHOD_FOR_COFFEE, (name,)).fetchone()

def get_top_10_ratings(connection):
    with connection:
        return connection.execute(GET_TOP_10_RATINGS).fetchall()