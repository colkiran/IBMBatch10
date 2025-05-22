
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", database="playersdb", port=3306)

cursor = conn.cursor()
FL = open("playersData.txt", "r")

for query in FL.readlines():
    cursor.execute(query)

FL.close()
conn.commit()
conn.close()
