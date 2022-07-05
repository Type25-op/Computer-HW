#Computer science project 'Hospital management project'
# -Govind Goyal
from subprocess import check_output
import mysql.connector as db_
from pyfiglet import Figlet
db = db_.connect(host="localhost", port='3306',user = 'root',password = 'elephant')
cur = db.cursor(buffered=True)     
cur.execute("USE hospital_management")
Permissons = False
User = None

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#********************************************************Functions*********************************************************************************************
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def red(text):print("\033[91m {}\033[00m".format(text))
def blue(text):print("\033[96m {}\033[00m".format(text))
def Login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    cur.execute("select * from users")
    for x in cur:
        if x[1]==username and x[2]==password:
            global Permissons
            Permissons = True
            User  = x[1]
            blue("success")
            return
        else:
            pass
    red("invalid credentials")
    return
def Logout():
    Permissons = False
    User = None
    blue("success")
def Add_user():
    if Permissons == True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        phone = input("Enter phone: ")
        email  = input("Enter email: ")
        query="insert into users (name,pass, phone, email)values(%s,%s,%s,%s)"
        data =(username, password, phone, email)
        cur.execute(query,data)
        db.commit()
        blue("success")  
    else:red("LOGIN required")
def Add_doc():
    if Permissons ==True :
        username = input("Enter username: ")
        password = input("Enter password: ")
        phone = input("Enter phone: ")
        email  = input("Enter email: ")
        query="insert into docs (name,pass, phone, email)values(%s,%s,%s,%s)"
        data =(username, password, phone, email)
        cur.execute(query,data)
        db.commit()
        blue("success")
    else:red("LOGIN required")
def Add_patient():
    if Permissons == True:
        username = input("Enter username: ")
        phone = input("Enter phone: ")
        email  = input("Enter email: ")
        doctor = input("Enter doctor(in charge of the person): ")
        room = input("Enter room(where patient is in): ")
        query="insert into patients (name, phone, email,doctor,place)values(%s,%s,%s,%s,%s)"
        data =(username, phone, email,doctor,room)
        cur.execute(query,data)
        db.commit()
        blue("success")
    else:red("LOGIN required")
def Check_Patients():
    if Permissons == True:
        name = input("Enter name: ")
        cur.execute("select * from patients ")
        for x in cur:
            if x[1] == name:
                print(x)
                return
            else :pass
        red("NO VALID Patient")
    else:red("LOGIN required")
def Check_in():
    username = input("Enter username: ")
    password = input("Enter password: ")
    cur.execute("select * from docs")
    for x in cur:
        if x[1] == username and x[2] == password:
            query =f"update docs set working = '1' where name = '{username}';"
            cur.execute(query)
            db.commit()
            blue("Check in SUCESSFUL")
            return
        else:
            red("CHECK IN UNSUCESSFUL")
def Check_out():
    username = input("Enter username: ")
    password = input("Enter password: ")
    cur.execute("select * from docs")
    for x in cur:
        if x[1] == username and x[2] == password:
            query =f"update docs set working = '0' where name = '{username}'"
            cur.execute(query)
            db.commit()
            blue("Check Out SUCESSFUL")
            return
        else:
            red("Check Out UNSUCESSFUL")
def Active_Docs():
    if Permissons == True:
        cur.execute("select * from Docs")
        for x in cur:
            if x[5]=='1':
                print(x[1])
            else:pass
    else:red("LOGIN required")
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#********************************************************Termial*********************************************************************************************
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
working = True
Logo = Figlet(font='graffiti')
print(Logo.renderText("Hospital Management System"))
while working:
    print("Type the numbers to the corrsponding task to use them. Login,Logout,exit,Checkin(For Docs),and Checkout(For Docs)are available without the sign in")
    print("\t\b1:Login")
    print("\t\b2:Logout")
    print("\t\b3:Check in")
    print("\t\b4:Check out")
    print("\t\b5:Active Doctors list")
    print("\t\b6:Check Patient")
    print("\t\b7:Add Patient")
    print("\t\b8:Add user account")
    print("\t\b9:Add Doctor")
    print("\t\b0:Exit")
    cin = int(input(">>>"))
    if cin == 0:
        red("CLOSING THE PROGRAM")
        working = False
    elif cin == 1:
        Login()
    elif cin == 2:
        Logout()
    elif cin == 3:
        Check_in()
    elif cin == 4:
        Check_out()
    elif cin == 5:
        Active_Docs()
    elif cin == 6:
        Check_Patients()
    elif cin == 7:
        Add_patient()
    elif cin == 8:
        Add_user()
    elif cin == 9:
        Add_doc()