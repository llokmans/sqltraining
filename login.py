
import sqlite3
import hashlib


username = input("Enter your username: ")
password = input("Enter your password: ")

hashed = hashlib.sha256(password.encode()).hexdigest()

con = sqlite3.connect("users.db")
cur = con.cursor()

cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed))
result = cur.fetchone()

if result:
    print("Access Granted.")
else:
    print("Access Denied.")

con.close()
