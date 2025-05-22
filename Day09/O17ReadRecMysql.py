
import pymysql
from prettytable import  from_db_cursor

conn = pymysql.connect(host="localhost", user="root", password="", database="playersdb", port=3306)

cursor = conn.cursor()

query = "select * from player"

cursor.execute(query)

prtyTbl = from_db_cursor(cursor)

# for rec in cursor.fetchall():
#     print(rec)

conn.close()

print(prtyTbl)
