import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (without specifying a database)
        mydb = mysql.connector.connect(
            host="127.0.0.1",  # or 'localhost'
            user="root",
            password="Pitter.5051",  # Replace with your actual password
        )

        if mydb.is_connected():
            mycursor = mydb.cursor()
            # Create the database if it doesn't exist (safe against duplication)
            mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    
    finally:
        # Ensure the database connection is closed
        if 'mydb' in locals() and mydb.is_connected():
            mycursor.close()
            mydb.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    create_database()
