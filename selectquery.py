import mysql.connector

db= mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "user"
)

data = db.cursor()

selectquery = "select * from mytable"
data.execute(selectquery)

fetchedata = data.fetchall()

for i in fetchedata:
    print(i)
    
db.close()