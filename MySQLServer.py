import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        mydb = mysql.connector.connect(
            host="127.0.0.1",  # or 'localhost'
            user="root",
            password="Pitter.5051",  # Replace with your actual password
        )
        if mydb.is_connected():
            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

        except mysql.connector.Error

if __name__ == "__main__":
    create_database()
