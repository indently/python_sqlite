import sqlite3
from contextlib import closing

# Connects to a database, if not created, it creates a new one
connection = sqlite3.connect("info.db")

cursor = connection.cursor()
# cursor.execute("CREATE TABLE people (name TEXT, age INTEGER, skills STRING)")

# # Insert data into the database
# cursor.execute("INSERT INTO people VALUES ('Mario', '23', 'Chef')")
# cursor.execute("INSERT INTO people VALUES ('Luigi', '25', 'Waiter')")
# cursor.execute("INSERT INTO people VALUES ('Toad', '20', 'Servant')")

# Fetch the data and print it
rows = cursor.execute("SELECT name, age, skills FROM people").fetchall()
print(rows)

# Pick a person from the database
target_person = "Luigi"
rows = cursor.execute("SELECT name, age, skills FROM people WHERE name = ?", (target_person,), ).fetchall()

print(rows[0][0])

# Change data
new_age = 30
selected_name = "Luigi"
cursor.execute(
    "UPDATE people SET age = ? WHERE name = ?",
    (new_age, selected_name)
)

rows = cursor.execute("SELECT name, age, skills FROM people").fetchall()
print(rows)

# Delete data
name_fired = "Toad"
cursor.execute(
    "DELETE FROM people WHERE name = ?",
    (name_fired,)
)

rows = cursor.execute("SELECT name, age, skills FROM people").fetchall()
print(rows)

# Commits/saves the data to the database
connection.commit()

# Closing the programme
with closing(sqlite3.connect("info.db")) as connection:
    with closing(connection.cursor()) as cursor:
        rows = cursor.execute("SELECT 1").fetchall()
        print(rows)
