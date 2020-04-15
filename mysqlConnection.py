import mysql.connector


mydb = mysql.connector.connect(host="localhost", user="root", passwd="Pass@123", database="bookworm")

mycursor = mydb.cursor()
mycursor.execute("show tables")

for i in mycursor:
    print(i)