import mysql.connector


mydb = mysql.connector.connect(host="localhost", user="root", passwd="Pass@123", database="bookworm")

mycursor = mydb.cursor()
mycursor.execute("select * from userdetails")

for i in mycursor:
    print(i)