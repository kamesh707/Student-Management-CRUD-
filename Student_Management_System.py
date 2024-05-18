import mysql.connector as sql
passwd=str(input("database password:"))
con=sql.connect(host="localhost",user="root",passwd=passwd)
c=con.cursor()
sql1="show databases"
c.execute(sql1)
sql2="create database mysch"
c.execute(sql2)
sql3="use mysch"
c.execute(sql3)
sql4="""create table students(Name Varchar(50),Registration Varchar(50),Class varchar(50),RollNumber integer,Date varchar(20))"""
c.execute(sql4)
sql5="""create table fees(Name varchar(20),Registration varchar(25),Fee varchar(8),Date varchar(20),phone varchar(20))"""
c.execute(sql5)
sql6="create table bills(Detail varchar(20),Cost integer,Date varchar(20))"""
c.execute(sql6)
sql7="""create table teacher(Name varchar(100),Work varchar(20),Salary varchar(20))"""
c.execute(sql7)
con.commit()
#LOGIN
def signin():
    print("\n")
    print("---------------------------------->>>>>>>>>WELCOME TO HAPPINESS SCHOOL INTERNATIONAL[H.S.I]<<<<<<<<<<--------------------")
    print("\n")
    p=input("system password")
    if p=="hsi0007":
        options()
    else:
        signin()

def options():
    print("""                $ HAPPINESS SCHOOL INTERNATIONAL $
                    ----------------------------------------------------
                    1. Add Student                  5. Display Students
                    2. Pay Fees                     6. Display Fees
                    3. Add Bill                     7. Display Bills
                    4. Add Teacher                  8. Display Teachers

                    ------------------------------------------------------
    """)
    choice=input("select option:")
    while True:
        if(choice=='1'):
            addstudent()
        elif (choice=='2'):
            payfees()
        elif (choice=='3'):
            addbill()
        elif (choice=='4'):
            addteacher()
        elif (choice=='5'):
            dstudents()
        elif (chocie=='6'):
            dfees()
        elif(choice=='7'):
            dbills()
        elif (choice=='8'):
            dteacher()
        else:
            print("enter again.......")
            options()


def addstudent():
    n=input("Name:")
    r=input("Registration:")
    c=input("class:")
    rn=input("Roll Number:")
    d=input("Date:")
    sql='insert into Students values(%s,%s,%s,%s,%s)'
    data=(n,r,c,rn,d)
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Inserted Successfully")
    options()

def payfees():
    n=input("Name:")
    r=input("Registration:")
    f=input("Fees")
    d=input("Date")
    p=input("phone")
    data=(n,r,f,d,p)
    sql='insert into fees values(%s,%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("data inserted successfully")
    options()

def addbill():
    dt=input("detail:")
    c=input("cost:")
    d=input("Date:")
    data=(dt,c,d)
    sql='insert into bills values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print('Data Inserted Successfully')
    options()

def addteacher():
    n=input("Name:")
    w=input("Work:")
    s=input("Salary:")
    data=(n,w,s)
    sql='insert into teacher values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print('data inserted successfully')
    options()

def dstudents():
    cl=input("Class:")
    sql='select * from students"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        if i[2] ==cl:
            print("Name:",i[0],"Registration:",i[1],"Class:",i[2],"RollNumber:",i[3],"Date:",i[4])
            print("--------------------------------------------------------------------------")
    options()

def dfees():
    sd=input("Date:")
    sql='Select * from fees'
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        if i[3] == sd:
            print("Name:",i[0],"Registration:",i[1],"Fee:",i[2],"Date:",i[3],"Phone:",i[4])
            print("-------------------------------------------------------------------")
    options()

def dbills():
    sql="select * from bills"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print("detail:",i[0],"cost:",i[1],"Date:",i[2])
        print("----------------------------------")

    options()

def dteacher():
    sql='select * from teacher'
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print("Name:",i[0],"Work:",i[1],"salary:",i[2])
        print("-----------------------------------")
    options()
        
