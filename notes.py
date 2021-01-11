import sqlite3
from contextlib import closing

connection = sqlite3.connect("info.db")

cursor = connection.cursor()
try:
    cursor.execute("CREATE TABLE people (name TEXT, age INTEGER, skills STRING)")
except Exception as e:
    print(e)


def insert_db():
    name = input("Name >>")
    age = input("Age >>")
    skills = input("Skills >>")

    if name != "" and age != "" and skills != "":
        cursor.execute(f"INSERT INTO people VALUES ('{name}', '{age}', '{skills}')")
        print(name + " has been added to the database!")
        connection.commit()

    else:
        print("One of the fields is empty, please try again.")
        insert_db()


def edit_db():
    name = input("Type the name of the person that you would like to edit >>")



def delete_db():
    name = input("Type the name of the person that you would like to delete >>")
    if name != "":
        cursor.execute(
            "DELETE FROM people WHERE name = ?",
            (name,))
        connection.commit()



def display_db():
    rows = cursor.execute("SELECT name, age, skills FROM people").fetchall()
    print(rows)


while True:
    options = input("""
    Type '1' to insert to database
    Type '2' to display database 
    Type '3' to delete user 
    >>""")

    if options == "1":
        insert_db()
    if options == "2":
        display_db()
    if options == "3":
        delete_db()

    print("-----------------------")