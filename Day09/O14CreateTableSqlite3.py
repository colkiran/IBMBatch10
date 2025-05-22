import sqlite3

conn = sqlite3.connect("playersdb.sqlite3")

cursor = conn.cursor()

query = """
create table player (
plyid varchar(7) PRIMARY KEY,
plyname varchar(50) not null, 
sport varchar(30) not null, 
achievements varchar(50) not null
)
"""

cursor.execute(query)
conn.close()
