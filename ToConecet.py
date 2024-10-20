import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pitter.5051",
    database="alx_book_store"
)

mycursor = mydb.cursor()
# Execute SQL statements using the execute() method on the cursor

# Close connection to the databasse  
mycursor.close()
mydb.close()