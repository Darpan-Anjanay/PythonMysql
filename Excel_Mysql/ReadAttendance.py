# Read Attendance from Excel File

import pandas as pd
def ReadAttendance():
    df = pd.read_excel('Attendance.xlsx')
    attendance = []

    for index, row in df.iterrows():
        attendance.append({'Empid': int(row['Empid']), 'Status': row['Status'], 'Date': row['Date'].strftime('%Y-%m-%d')})
    return attendance

# My sql connecting
import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'your_username',
    password = 'your_password',
    database = 'your_database' 
)


mycursor = mydb.cursor()
   
# Dumping data into Mysql database table Attendance
data = ReadAttendance()
for d in data:
    mycursor.execute(
        "INSERT INTO Attendance (Empid, Status, Date) VALUES (%s, %s, %s)",
        (d['Empid'], d['Status'], d['Date'])
    )
mydb.commit()
