import sqlite3

con = sqlite3.connect("users.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
con.commit()
con.close()

print("Database and users table created successfully.")