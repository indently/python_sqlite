import sqlite3
import sys

connection = sqlite3.connect("info.db")
cursor = connection.cursor()

try:
    cursor.execute("CREATE TABLE people (name TEXT, age INTEGER, skills STRING)")
except Exception as e:
    print(e)


def user_is_unique(name):
    rows = cursor.execute("SELECT name, age, skills FROM people").fetchall()

    for user in rows:
        if user[0] == name:
            return False
    return True


def insert_db():
    name = input("Name >>")

    if user_is_unique(str(name)):
        age = input("Age >>")
        skills = input("Skills >>")

        if name != "" and age != "" and skills != "":
            cursor.execute(f"INSERT INTO people VALUES ('{name}', '{age}', '{skills}')")
            connection.commit()
            print(name + " has been added to the database!")

        else:
            print("One of the fields is empty, please try again.")
            insert_db()

    else:
        print("Name is already in the database!")


def edit_db():
    name = input("Type the name of the person that you would like to edit >>")
    field = input("Which field would you like to edit: name, age, or skills? >>")
    updated_field = input("What would you like to update it to? >>")

    try:
        cursor.execute(
            f"UPDATE people SET {field} = ? WHERE name = ?",
            (updated_field, name)
        )
        connection.commit()
        print("Successfully updated user!")
    except Exception as e:
        print(e)


def get_user_info_db():
    target_person = input("Who do you want to see information about? >>")
    rows = cursor.execute("SELECT name, age, skills FROM people WHERE name = ?", (target_person,), ).fetchall()

    name = rows[0][0]
    age = rows[0][1]
    skills = rows[0][2]

    print(f"{name} is {age} years old, and works as a {skills}.")


def delete_db():
    name = input("Type the name of the person that you would like to delete >>")
    if name != "":
        cursor.execute(
            "DELETE FROM people WHERE name = ?",
            (name,))
        connection.commit()
        print("User successfully deleted!")


def display_db():
    rows = cursor.execute("SELECT name, age, skills FROM people ORDER BY name ASC").fetchall()

    print("Users: ")
    for user in rows:
        print(f"- {user[0]} / {user[1]} / {user[2]}")


def exit_db():
    cursor.close()
    connection.close()
    sys.exit()


def select_options():
    options = input("""
-----------------------
Type '0' to exit
Type '1' to insert a new user
Type '2' to display users
Type '3' to delete user 
Type '4' to edit user 
Type '5' to get user information
-----------------------
>>""")

    if options == "0":
        exit_db()
    if options == "1":
        insert_db()
    if options == "2":
        display_db()
    if options == "3":
        delete_db()
    if options == "4":
        edit_db()
    if options == "5":
        get_user_info_db()


# Infinite loop
while True:
    select_options()
