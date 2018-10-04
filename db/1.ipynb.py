#ques_1.
import sqlite3
try:
    con=sqlite3.connect('Students.db')
    cur=con.cursor()
    query='create table Marks(Name varchar(10),Marks int(3))'
    cur.execute(query)
    print("Succesful")
    con.commit()
except:
    if con:
        con.rollback()
        print("Rolled Back")
finally:
    if con:
        cur.close()
        con.close()
        print("Done!")
#ques_2.
Students=[]
for i in range(0,10):
    rec1=input("Enter Student Name ")
    rec2=int(input("Enter Marks"))
    records=(rec1,rec2)
    Students.append(records)
#ques_3.
import sqlite3
try:
    con=sqlite3.connect("Students.db")
    cur=con.cursor()
    query='insert into Marks(Name,Marks) values (?,?)'
    cur.executemany(query,Students)
    print("Added")
    con.commit()
except:
    con.rollback()
    print("RolledBack")
finally:
    cur.close()
    con.close()
    print("Done!!")
#ques_4.
import sqlite3
try:
    con=sqlite3.connect('Students.db')
    C=con.cursor()
    query='select * from Marks where Marks>80'
    C.execute(query)
    Data=C.fetchall()
    con.commit()
except:
    if con:
        con.rollback()
finally:
    print("Students with Marks More Than 80:")
    print('NAME     Marks')
    for i in range(0,len(Data)):
        print('{}         {}'.format(Data[i][0],Data[i][1]))
    if con:
        C.close()
        con.close()
        print("DONE!")
