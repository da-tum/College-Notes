
import sqlite3
conn = sqlite3.connect("./Handlings/ppt 38/Database Handling/students.db")
cursor = conn.cursor()

#Creating a Table
cursor.execute('''CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)''')
conn.commit()

#Inserting Data into the Table
cursor.execute("INSERT INTO student (name, age) VALUES (?, ?)",("Alice", 22))
cursor.execute("INSERT INTO student (name, age) VALUES (?, ?)",("Ankit", 26))
cursor.execute("INSERT INTO student (name, age) VALUES (?, ?)",("Manas", 30))
cursor.execute("INSERT INTO student (name, age) VALUES (?, ?)",("Shourya", 122))
conn.commit()

#Reading Data (SELECT)
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()
print(rows,'this is the list')
for row in rows:
    print(row)
     

#Updating Data
cursor.execute("UPDATE student SET age = ? WHERE name = ?",(23, "Alice"))
conn.commit()

#Checking via Reading Data Again
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()
print(rows)
for row in rows:
    print(row," after update")

#Deleting Data
cursor.execute("DELETE FROM student WHERE name = ?",("Alice",))
conn.commit()

#Checking via Reading Data Again
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()
print(rows,"after deletion")  # Should be empty after deletion

#Closing the Database Connection
conn.close()

#not working as DB closed
#cursor.execute("SELECT * FROM student")
