import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="new_password"
    )
    cursor = connection.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as error:
    print("Failed to connect to MySQL server:", error)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
