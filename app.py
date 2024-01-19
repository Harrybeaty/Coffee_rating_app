import database

MENU_PROMPT = """-- Coffee Tracker --

Please choose one of these options

1) Add a new coffee.
2) See all coffees.
3) Find a coffee by name.
4) See which method is the best.
5) Find the top 10 highest rated.
6) Exit

Your selection: 
"""


def menu():
    connection = database.connect()                   # Open connection to sqlite.
    database.create_tables(connection)     
# Check user_input does not = exit.
    while (user_input := input(MENU_PROMPT)) != "6":  # := is used to give a varibale a value within a statement.
        if user_input == "1":
            name = input("Enter coffee name: ")
            method = input("Enter the method use to prepare it: ")
            strength =  int(input("Enter strength (0-10): "))
            harry_rating = int(input("Enter my rating score (0-100): "))
            mum_rating = int(input("Enter Mum's rating score (0-100): "))

            database.add_bean(connection, name, method, strength, mum_rating, harry_rating)  # calls function from database.py, passing variables and the connection to sql.
        elif user_input == "2":
            coffees = database.get_all_coffee(connection) # Returns a list.

            for coffee in coffees:
                print(f"""\nName: {coffee[1]}
Method: {coffee[2]} 
Strength: {coffee[3]}/10 
Mum's rating: {coffee[4]}/100 
Harry's rating: {coffee[5]}/100 
\n""")
        elif user_input == "3":
            name = input("Enter coffee by name to find: ")
            coffees = database.get_coffee_by_name(connection, name)

            for coffee in coffees:
                print(f"""\nName: {coffee[1]}
Method: {coffee[2]} 
Strength: {coffee[3]}/10 
Mum's rating: {coffee[4]}/100 
Harry's rating: {coffee[5]}/100 
\n""")
        elif user_input == "4":
            name = input("Enter name of coffee: ")
            best_method = database.get_best_method_for_coffee(connection, name)

            print(f"The best method for preperation of {name} is {best_method[2]}\n")

        elif user_input == "5":
            coffees = database.get_top_10_ratings(connection)

            for coffee in coffees:
                print(f"""\nName: {coffee[1]}
Method: {coffee[2]} 
Strength: {coffee[3]}/10 
Mum's rating: {coffee[4]}/100 
Harry's rating: {coffee[5]}/100
\n""")
        else:
            print("Invalid input, please try again")

menu()