from mysql.connector import connect,Error
from getpass import getpass
try:
    conn = connect(host="localhost",
                                  port=3306,
                                  user="root",
                                  password="root"
                                  ,db="user",
                                  auth_plugin='mysql_native_password')
    
    with connect(
        host = "localhost",
        port= 3306,
        user = "root",
        password = "root",  
        database = "user",  
    ) as connection:
        print(connection)
except Error as e:
    print(e)
