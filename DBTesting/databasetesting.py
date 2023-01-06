import mysql.connector

# host,database,username,password

#conn = mysql.connector.connect(host='localhost', database='APIDevelop', user='root', password='root')

from Utilities.configurations import getConnection

# comes from configurations file
conn=getConnection()

# to check if db is connected
print(conn.is_connected())  # True

cursor = conn.cursor()
cursor.execute('select * from worker')

'''
# first row will be returned
onerow=cursor.fetchone()
print(onerow)
# tuple- ('selenium', datetime.date(2021, 7, 18), 120, 'Africa')
print(onerow[3]) # Africa

# remaining rows will be returned
print(cursor.fetchall())
# list of tuples- [('Protractor', datetime.date(2021, 7, 18), 45, 'Africa'), ('Appium', datetime.date(2021, 7, 18), 99, 'Asia'), ('Jmeter', datetime.date(2021, 7, 18), 76, 'US')]
'''

allrows = cursor.fetchall()
print(allrows)
print(type(allrows))  # <class 'list'>

sum = 0
for row in allrows:
    print(row[3])  # gives amount of every row  # 120 45 99 76
    sum = sum + row[3]

print(sum)  # 340
assert sum==1838750

updatequery ="update customerInfo set Location = %s where CourseName = %s"
data = ("Saudi Arabia", "Jmeter")
cursor.execute(updatequery,data)

conn.commit()
conn.close()  # close db connection.
