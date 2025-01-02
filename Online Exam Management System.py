import mysql.connector as c
from datetime import date, datetime, timedelta
import os
import platform

def DatabaseCreate():
    con = c.connect(host = 'localhost', port = 3306, user = 'root',password ='root',database = 'online_exam')
    Cursor = con.cursor()
    Cursor.execute("CREATE DATABASE IF NOT EXISTS online_exam")
    Cursor.execute("")
    Cursor.close()
    con.close()

def TablesCreate():
    con = c.connect(host = 'localhost', port = 3306, user = 'root', password = 'root',database = 'online_exam')
    Cursor = con.cursor()
    Cursor.execute("CREATE TABLE IF NOT EXISTS Student(User_ID varchar(10) PRIMARY KEY, Password varchar(20), Email_Address varchar(40), Name text(40), Roll_Number varchar(20), Phone varchar(10))")
    Cursor.execute("CREATE TABLE IF NOT EXISTS Subject(Subject_ID varchar(10) PRIMARY KEY, Subject_name text(20), Credits int(2), Teacher text(40))")
    Cursor.execute("CREATE TABLE IF NOT EXISTS Exam(Exam_ID varchar(10) PRIMARY KEY, User_ID varchar(10), Subject_ID varchar(10), Exam_Link varchar(50))")
    Cursor.close()
    con.close()

def MenuStudent():
    while True:
        print("\t\t\t Student Record Management\n")
        print("==============================================")
        print("1. Add Student")
        print("2. Search Student Record")
        print("3. Delete Student Record")
        print("4. Update Update Record")
        print("5. Return to Main Menu")
        print("=======================================")
        choice = int(input("Enter Choice between 1 to 5 -------> : "))
        if choice == 1:
            insertData()
        elif choice == 2:
            SearchStudentRec()
        elif choice == 3:
            deleteStudent()
        elif choice == 4:
            UpdateStudent()
        elif choice == 5:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Enter any key to continue")

def MenuSubject():
    while True:
        print("\t\t\t Subject Record Management\n")
        print("==========================================")
        print("1. Add Subject Record")
        print("2. Search Subject Record")
        print("3. Delete Subject Record")
        print("4. Update Subject Record")
        print("5. Return to Main Menu")
        print("==========================================")
        choice = int(input("Enter Choice between 1 to 5 ------> : "))
        if choice == 1:
            insertSubject()
        elif choice == 2:
            SearchSubject()
        elif choice == 3:
            deleteSubject()
        elif choice == 4:
            UpdateSubject()
        elif choice == 5:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Enter any key to continue")

def MenuExam():
    while True:
        print("\t\t\t Member Record Management\n")
        print("==========================================")
        print("1. Add Exam")
        print("2. Delete Exam")
        print("3. View Exam")
        print("4. Return to Main Menu")
        print("==========================================")
        choice = int(input("Enter Choice between 1 to 4 ------> : "))
        if choice == 1:
            AddExam()
        elif choice == 2:
            DeleteExam()
        elif choice == 3:
            ViewExam()
        elif choice == 4:
            return
        else:
            print("Wrong Choice.....Enter Your Choice again")
            x = input("Enter any key to continue")

def clrscreen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def insertData():
    try:
        con = c.connect(host = 'localhost', port = 3306, user = 'root', password ='root',database = 'online_exam')
        Cursor = con.cursor()
        User_ID = input("Enter User_ID : ")
        Password = input("Enter Password : ")
        Email_Address = input("Enter Email_Address : ")
        Name = input("Name : ")
        Roll_Number = input("Enter Roll_Number : ")
        Phone = input("Enter Phone_Number : ")
        Qry = ("INSERT INTO Student VALUES (%s, %s, %s, %s, %s, %s)")
        data = (User_ID, Password, Email_Address, Name, Roll_Number,Phone)
        Cursor.execute(Qry,data)
        con.commit()
        Cursor.close()
        con.close()
        print("Record Inserted.")
    except c.errors.Error as err:
        if err.errno == err.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == err.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    con.close()
    
def deleteStudent():
    try:
        con =c.connect(host = 'localhost', port = 3306, user = 'root',password ='root',database = 'online_exam')
        Cursor = con.cursor()
        User_ID = input("Enter User_ID of Student to be deleted : ")
        Qry = ("""DELETE FROM Student WHERE User_ID = %s""")
        del_rec = (User_ID,)
        Cursor .execute(Qry, del_rec)
        con.commit()
        Cursor.close()
        con.close()
        print(Cursor.rowcount, "Record(s) Deleted Successfully.")
    except c.errors.Error as err:
        if err.errno ==err.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == err.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    con.close()

def SearchStudentRec():
    try:
        con = c.connect(host = 'localhost', port = 3306, user = 'root',password ='root',database = 'online_exam')
        Cursor = con.cursor()
        User_ID = input("Enter User_ID of Student to be searched : ")
        query = ("SELECT * FROM Student WHERE User_ID = %s ")
        rec_srch = (User_ID,)
        Cursor.execute(query, rec_srch)
        Rec_count = 0
        for(User_ID, Password, Email_Address, Name, Roll_Number, Phone) in Cursor:
            Rec_count += 1
            print("===========================================")
            print("User_ID : ", User_ID)
            print("Password : ", Password)
            print("Email_Address : ", Email_Address)
            print("Name: ", Name)
            print("Roll_Number : ", Roll_Number)
            print("Phone : ", Phone)
            print("==========================================")
            if Rec_count%2 == 0:
                input("Press any key continue")
                clrscreen()
                print(Rec_count, "Record(s) found")
            elif Cursor.rowcount == 0:
                print("No student found with the given User_ID")
            con.commit()
            Cursor.close()
            con.close()
    except c.errors.Error  as err:
        if err.errno == err.ER_ACCESS_DENIED_Error:
            print("Something is wrong with your user name or password")
        elif err.errno == err.ER_BAD_DB_Error:
            print("Database does not exist")
        else:
            print(f"AAn error occured:{err}")
    con.close()

def UpdateStudent():
    try:
        con = c.connect(host = 'localhost', port = 3306, user = 'root',password ='root',database = 'online_exam')
        Cursor = con.cursor()
        User_ID = input("Enter User_ID of the Student to be Updated : ")
        print("Enter new data")
        New_User_ID = input("Enter User_ID : ")
        Password = input("Enter Password : ")
        Email_Address = input("Enter Email_Address : ")
        Name = input("Name : ")
        Roll_Number = input("Enter Roll_Number : ")
        Phone = input("Enter Phone_Number : ")
        Qry = ("UPDATE Student SET User_ID=%s, Password=%s, Email_Address=%s,Name=%s, Roll_Number=%s, Phone=%s WHERE User_ID = %s")
        data = (New_User_ID, Password, Email_Address, Name, Roll_Number, Phone,User_ID)
        Cursor.execute(Qry,data)
        con.commit()
        Cursor.close()
        con.close()
        print(Cursor.rowcount, "Record(s) Updated Successfully.")
    except c.errors.Error  as err:
        if err.errno == err.ER_ACCESS_DENIED_Error:
            print("Something is wrong with your user name or password")
        elif err.errno == err.ER_BAD_DB_Error:
            print("Database does not exist")
        else:
            print(err)
    con.close()

def insertSubject():
    try:
        con = c.connect(host = 'localhost', port = 3306, user = 'root',password ='root',database = 'online_exam')
        Cursor = con.cursor()
        Subject_ID = input("Enter Subject_ID : ")
        Subject_name = input("Enter Subject Name : ")
        Credits = int(input("Enter Credits : "))
        Teacher = input("Enter Teacher Name : ")
        Qry = ("INSERT INTO Subject VALUES(%s, %s, %s, %s)")
        data = (Subject_ID,Subject_name, Credits,Teacher)
        Cursor.execute(Qry, data)
        con.commit()
        Cursor.close()
        con.close()
        print("Record Inserted.")
    except c.errors.Error  as err:
        if err.errno == err.ER_ACCESS_DENIED_Error:
            print("Something is wrong with your user name or password")
        elif err.errno == err.ER_BAD_DB_Error:
            print("Database does not exist")
        else:
            print(err)
    con.close()

def deleteSubject():
    try:
        con = c.connect(host = 'localhost', port = 3306, user = 'root',password ='root',database = 'online_exam')
        Cursor = con.cursor()
        Subject_ID = input("Enter Subject_ID to be deleted : ")
        Qry =("""DELETE FROM Subject WHERE Subject_ID = %s""")
        del_rec = (Subject_ID,)
        Cursor.execute(Qry, del_rec)
        con.commit()
        Cursor.close()
        con.close()
        print(Cursor.rowcount, "Record(s) Deleted Successfully.")
    except c.errors.Error  as err:
        if err.errno == err.ER_ACCESS_DENIED_Error:
            print("Something is wrong with your user name or password")
        elif err.errno == err.ER_BAD_DB_Error:
            print("Database does not exist")
        else:
            print(err)
    con.close()

def SearchSubject():
    try:
        con = c.connect(host = 'localhost', port = 3306, user = 'root',password ='root',database = 'online_exam')
        Cursor = con.cursor()
        Subject_ID = input("Enter Subject_ID to be Searched : ")
        query = ("SELECT * FROM Subject where Subject_ID = %s")
        rec_srch = (Subject_ID,)
        Cursor.execute(query, rec_srch)
        Rec_count = 0
        for(Subject_ID,Subject_name, Credits,Teacher) in Cursor:
            Rec_count += 1
            print("=============================================")
            print("Subject_ID : ", Subject_ID)
            print("Subject_name : ", Subject_name)
            print("Credits : ", Credits)
            print("Teacher : ", Teacher)
            print("=============================================")
            if Rec_count%2 == 0:
                input("Press any key to continue: ")
                clrscreen()
                print(Rec_count, "Record(s) found")
            con.commit()
            Cursor.close()
 
            con.close()
    except c.errors.Error  as err:
        if err.errno == err.ER_ACCESS_DENIED_Error:
            print("Something is wrong with your user name or password")
        elif err.errno == err.ER_BAD_DB_Error:
            print("Database does not exist")
        else:
            print(err)
        con.close()

def UpdateSubject():
    try:
        con = c.connect(host = 'localhost', port = 3306, user = 'root',password ='root',database = 'online_exam')
        Cursor = con.cursor()
        Subject_ID = input("Enter Subject_ID of Subject to be Updated : ")
        print("Enter new data")
        New_Subject_ID = input("Enter Subject_ID : ")
        Subject_name = input("Enter Subject Name : ")
        Credits = int(input("Enter Credits : "))
        Teacher = input("Enter Teacher Name : ")
        Qry = ("UPDATE Subject SET Subject_ID=%s, Subject_name=%s, Credits=%s,Teacher=%s WHERE Subject_ID=%s")
        data = (New_Subject_ID,Subject_name, Credits,Teacher, Subject_ID)
        Cursor.execute(Qry,data)
        con.commit()
        Cursor.close()
        con.close()
        print(Cursor.rowcount, "Record(s) Updated Successfully.")
    except c.errors.Error  as err:
        if err.errno == err.ER_ACCESS_DENIED_Error:
            print("Something is wrong with your user name or password")
        elif err.errno == err.ER_BAD_DB_Error:
            print("Database does not exist")
        else:
            print(err)
    con.close()

def AddExam():
    con = c.connect(host = 'localhost', port = 3306, user = 'root', password ='root',database = 'online_exam')
    Cursor = con.cursor()
    Exam_ID = input("Enter Exam_ID : ")
    User_ID = input("Enter User_ID : ")
    Subject_ID = input("Enter Subject_ID : ")
    Exam_Link= input("Enter Exam Link : ")
    Qry = ("INSERT INTO Exam VALUES (%s, %s, %s, %s)")
    data = (Exam_ID, User_ID, Subject_ID, Exam_Link)
    Cursor.execute(Qry,data)
    con.commit()
    Cursor.close()
    con.close()
    print("Record Inserted.")
    con.close()

def DeleteExam():
    con = c.connect(host = 'localhost', port = 3306, user = 'root',password ='root',database = 'online_exam')
    Cursor = con.cursor()
    Exam_ID = input("Enter Exam_ID of Exam to be deleted : ")
    Qry = ("""DELETE FROM Exam WHERE Exam_ID = %s""")
    del_rec = (Exam_ID,)
    Cursor .execute(Qry, del_rec)
    con.commit()
    Cursor.close()
    con.close()
    print(Cursor.rowcount, "Record(s) Deleted Successfully.")
    con.close()

def ViewExam():
    try:
        con = c.connect(host = 'localhost', port = 3306, user = 'root',password ='root',database = 'online_exam')
        Cursor = con.cursor()
        Exam_ID = input("Enter Exam_ID of Exam to be searched : ")
        query = ("SELECT * FROM Exam WHERE Exam_ID = %s ")
        rec_srch = (Exam_ID,)
        Cursor.execute(query, rec_srch)
        Rec_count = 0
        for(Exam_ID, User_ID,Subject_ID, Exam_Link) in Cursor:
            Rec_count += 1
            print("===========================================")
            print("Exam_ID : ", Exam_ID)
            print("User_ID : ", User_ID)
            print("Subject_ID : ", Subject_ID)
            print("Exam_Link: ", Exam_Link)
            print("=================-=========================")
            if Rec_count%2 == 0:
                input("Press any key continue")
                clrscreen()
                print(Rec_count, "Record(s) found")
                con.commit()
                Cursor.close()
                con.close()
    except c.errors.Error  as err:
        if err.errno == err.ER_ACCESS_DENIED_Error:
            print("Something is wrong with your user name or password")
        elif err.errno == err.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
            con.close()

DatabaseCreate()
TablesCreate()
while True:
    print("\t\t\t Online Exam Management\n")
    print("============================================")
    print("1. Student Management")
    print("2. Subject Management")
    print("3. Exam Management")
    print("4. Exit")
    choice = int(input("Enter Choice between 1 to 4 -------> : "))
    if choice == 1:
        MenuStudent()
    elif choice == 2:
        MenuSubject()
    elif choice == 3:
        MenuExam()
    elif choice == 4:
        break
    else:
        print("Wrong Choice.....Enter Your Choice again")
        x = input("Press any key to continue")
