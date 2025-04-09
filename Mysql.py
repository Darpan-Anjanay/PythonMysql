import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Dell@123",
  database = 'clone'
  
)


mycursor = mydb.cursor()

mycursor.execute("select * from base_topic")

for x in mycursor:
  print(x)