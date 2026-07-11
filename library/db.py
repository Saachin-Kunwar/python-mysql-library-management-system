import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="library_db"
)

cursor = conn.cursor()




print("Database Connected Successfully")