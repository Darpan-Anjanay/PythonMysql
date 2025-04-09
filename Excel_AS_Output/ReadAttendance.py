
# connecting database
import mysql.connector 
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'your_username',
    password = 'your_password',
    database = 'your_database' 
)

# Getting data from database
mycursor = mydb.cursor()
mycursor.execute('select * from Attendance')
data =   mycursor.fetchall()


# Excel as output
import pandas as pd
df = pd.DataFrame(data,columns=['Empid','Status','Date'])
df.to_excel('Attendance.xlsx',index=False)