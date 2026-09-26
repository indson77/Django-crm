import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = "root" ,
    password="santosh8949"
)

# prepare a cursior object 

cursorObj = database.cursor()

# create a database 
cursorObj.execute("CREATE DATABASE IF NOT EXISTS indson")

print("All Done !!")