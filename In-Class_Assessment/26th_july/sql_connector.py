import mysql.connector as sql

db = sql.connect(
    host='*****',
    user='****',
    password='*********',
    database='school'
)
cursor = db.cursor()
cursor.execute('SELECT * FROM lab1')
data = cursor.fetchall()
print(data)
