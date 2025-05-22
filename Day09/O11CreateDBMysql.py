
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", port=3306)

query = "create database playersdb"

cursor = conn.cursor()

cursor.execute(query)

conn.close()
