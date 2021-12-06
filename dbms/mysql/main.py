import mysql.connector
from data import *
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

# get list Database
'''
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)
'''

# create database
'''
mycursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
'''

# create table
'''
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)
'''
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# insert
'''
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
mycursor.executemany(sql, data)
print(mycursor.rowcount, "was inserted.")
'''

# select
'''
mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
'''

# where
'''
sql = """
SELECT * FROM customers 
WHERE address ='Park Lane 38'
"""
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
'''

# where REGEXP
'''
sql = "SELECT * FROM customers WHERE address REGEXP '.*'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
'''

# delete

'''
sql = "DELETE FROM customers WHERE address = 'Sideway 1633'"
mycursor.execute(sql)
# sql = """
# DELETE FROM customers
# WHERE address = 'M.*21'
# """
mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
'''

# Limit ofset
'''
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 1")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
'''

mydb.commit()