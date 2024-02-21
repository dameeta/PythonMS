from mysql.connector import connect,Error
from getpass import getpass
try:
    with connect(
        host = "localhost",
        user = "root",
        password = "root",  
        database = "user",  
    ) as connection:
        print(connection)
except Error as e:
    print(e)
