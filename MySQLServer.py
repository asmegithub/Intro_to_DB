import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="new_password",
    database="alx_book_store"
)
if (connection):
    print("Database 'alx_book_store' created successfully!")
else:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="new_password",
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE alx_book_store")
    print("Database 'alx_book_store' created successfully!")

connection.close()
cursor.close()
