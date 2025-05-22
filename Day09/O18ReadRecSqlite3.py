

import sqlite3
from prettytable import  from_db_cursor

conn = sqlite3.connect("playersdb.sqlite3")

cursor = conn.cursor()

query = "select * from player"

cursor.execute(query)

prtyTbl = from_db_cursor(cursor)

# for rec in cursor.fetchall():
#     print(rec)

conn.close()

print(prtyTbl)
