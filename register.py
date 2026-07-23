import hashlib
import sqlite3

con = sqlite3.connect("users.db")
cur = con.cursor()

username = input("Enter your username: ")
password = input("Enter your password: ")

hashed = hashlib.sha256(password.encode()).hexdigest()

cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
con.commit()
con.close() 


