import  mysql.connector as my

db = my.Connect(
    host='127.0.0.1',
    user='root',
    password='root'
    )

cur = db.cursor()

#cur.execute("create database pythontest")
cur.execute("show databases")

for i in cur:
    print(i)

cur.close()
db.close()
#====================================================

import  mysql.connector as my

db = my.Connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database = "pythontest"
    )

cur = db.cursor()

cur.execute("create table student (roll int, name varchar(12), marks int)")
cur.execute('show tables')

for i in cur:
    print(i)
    
db.commit()
cur.close()
db.close()

#====================================================


import  mysql.connector as my

db = my.Connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database = "pythontest"
    )

cur = db.cursor()

sql="insert into student (roll,name,marks) values(2,'mandar',88)"
cur.execute(sql)
#cur.execute('show tables')

for i in cur:
    print(i)
    
db.commit()
cur.close()
#db.close()


#====================================================
import  mysql.connector as my

db = my.Connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database = "pythontest"
    )

cur = db.cursor()

val=[]

for i in range(0,2):
    roll=int(input("enter roll: "))
    name=input("enter name: ")
    marks=int(input("enter marks: "))
    val.append((roll,name,marks))
    
sql="Insert into student(roll ,name, marks) values(%s,%s,%s)"
cur.executemany(sql,val)

db.commit()
cur.close()

#====================================================

import  mysql.connector as my

db = my.Connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database = "pythontest"
    )

cur = db.cursor()
 
sql="update student set marks=100 where name='mandar'"
cur.execute(sql)

db.commit()
cur.close()

#====================================================

import  mysql.connector as my

db = my.Connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database = "pythontest"
    )

cur = db.cursor()
 
sql="select * from student"
cur.execute(sql)

result=cur.fetchall()
print(result)

cur.close()

#====================================================

import  mysql.connector as my

db = my.Connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database = "pythontest"
    )

cur = db.cursor()
 
sql="select * from student where marks <99"
cur.execute(sql)

result=cur.fetchall()
print(result)

cur.close()

#====================================================

import  mysql.connector as my

db = my.Connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database = "pythontest"
    )

cur = db.cursor()
 
sql="select * from student where REGEXP_LIKE(name,'^a.*')"
cur.execute(sql)

result=cur.fetchall()
print(result)

cur.close()


