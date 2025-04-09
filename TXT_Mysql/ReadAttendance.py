# Reading attendance from text file
def ReadAttendance():
    Attendance = []
    with open('Attendance.txt','r') as f:
        for i in f:
            if i.strip():
                att = i.strip().split(',')
                Attendance.append({'Empid':att[0],'Status':att[1],'Date':att[2]})
    return Attendance 

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