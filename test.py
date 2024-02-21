#import pandas as pd
import mysql.connector

def getConn_mysql():
    conn =mysql.connector.connect(host="localhost",
                                  port=3306,
                                  user="root",
                                  password="root"
                                  ,db="user",
                                  auth_plugin='mysql_native_password')
    cur = conn.cursor()
    print("connected successfully")
    #query1 = "SELECT * from movies;"
    """ query2 = "SELECT custid,bid,loan_amount as total_loan_amt\
        from loan order by total_loan_amt DESC;"
    #df1=pd.read_sql(query1,conn)
    df2=pd.read_sql(query2,conn)
    #data_types1 = {"id": int}
    data_types2 = {"custid":str}
    #df1=df1.astype(data_types1)
    df2=df2.astype(data_types2)

    #print(df1)
    print(df2)
    return cur,conn
 """

getConn_mysql()