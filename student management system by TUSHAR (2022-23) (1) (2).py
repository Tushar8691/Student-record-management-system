import mysql.connector as mc
mydatabase=mc.connect(host='localhost',user='root',password='2005')
mycursor=mydatabase.cursor()
mycursor.execute('create database if not exists studentrecord1')
mycursor.execute('use studentrecord1')
mycursor.execute('create table if not exists students(Rollno integer primary key,Name varchar(30),class varchar(4),fee integer)')
print('_________________________________________________________________')
print('*****************************login*******************************')
print('_________________________________________________________________')
ID=input('enter id:')
password=input('enter password:')
if ID=='project@' and password=='2022':
    print('\t\t\t\tlogin successful')
    print('_________________________________________________________________')
    print('********************STUDENT MANAGEMENT SYSTEM**********************')
    print('_________________________________________________________________')
else:
    print('*************************************************************')
    print('###################invaild id and password###################')
    print('********************************************************')
    quit()


def student_info():
    print('_________________________________________________________________')
    print('****************************MAIN MENU****************************')
    print('_________________________________________________________________')
    print('1.ADD RECORD')
    print('2.DISPLAY RECORD')
    print('3.SEARCH RECORD')
    print('4.DELETE RECORD')
    print('5.UPDATE RECORD')
    print('6.EXIT')
    print('_________________________________________________________________')
#add record
    ch=int(input('enter the choice'))
    if ch==1:
        print('_________________________________________________________________')
        print('**********************ENTER THE DETAILS**************************')
        print('_________________________________________________________________')
        r=input('enter the rollno')
        n=input('enter the name')
        c=input('enter the class')
        f=input('enter the fee')
        mycursor=mydatabase.cursor()
        sql='insert into students(Rollno,Name,Class,Fee)values(%s,%s,%s,%s)'
        valu=(r,n,c,f)
        mycursor.execute(sql,valu)
        mydatabase.commit()
        print('\t\t\t\tINFORMATION SAVED')
        print('_________________________________________________________________')
#display all information
    elif ch==2:
        mycursor=mydatabase.cursor()
        mycursor.execute('select*from students')
        mydata=mycursor.fetchall()
        nrec=mycursor.rowcount
        print('total records found are',nrec)
        print('%10s'%'Rollno','%10s'%'Name','%10s'%'Class','%10s'%'fee')
        print('_________________________________________________________')
        for row in mydata:
            print('%10s'%row[0],'%10s'%row[1],'%10s'%row[2],'%10s'%row[3])
            print('_________________________________________________________')
            
#search student by rollno
    elif ch==3:
        print('_________________________________________________________________')
        print('*******************SEARCH STUDENT BY ROLLNO**********************')
        print('_________________________________________________________________')
        rno=input('enter student rollno,whose data you want to search')
        mycursor=mydatabase.cursor()
        mycursor.execute('select*from students where Rollno={}'.format(rno))
        mydata=mycursor.fetchall()
        nrec=mycursor.rowcount
        print('total records found are',nrec)
        print('%10s'%'Rollno','%10s'%'Name','%10s'%'Class','%10s'%'fee')
        print('_________________________________________________________')
        for row in mydata:
            print('%10s'%row[0],'%10s'%row[1],'%10s'%row[2],'%10s'%row[3])
            print('_________________________________________________________')
#delete student information by rollno
    elif ch==4:
        print('_________________________________________________________________')
        print('********************Delete Record BY ROLLNO**********************')
        print('_________________________________________________________________')
        rno=input('enter student rollno,WHOSE DATA you want to DELETE')
        mycursor=mydatabase.cursor()
        mycursor.execute('delete from students where Rollno={}'.format(rno))
        mydatabase.commit()
        print('_________________________________________________________________')
        print('\t\t\t\trecord deleted successfuly')
        print('_________________________________________________________________')
#update student fee information by rollno
    elif ch==5:
        mycursor=mydatabase.cursor()
        rno=input('enter student rollno,WHOSE name/fee you want to update')
        print("1-Name,2-Fee")
        ch = input("Enter your choice(1-Name,2-Fee): ")
        lst = []
        for i in ch:
            lst.append(int(i))
        if 1 in lst:
            name = input("Enter name: ")
            mycursor.execute("update students set Name='{}' where Rollno={}".format(name, rno))
            mydatabase.commit()
        if 2 in lst:
            newfee=input('new fee:')
            mycursor.execute('update students set fee={} where Rollno={}'.format(newfee, rno))
            mydatabase.commit()
        mycursor.execute('select*from students where Rollno={}'.format(rno))
        mydata=mycursor.fetchall()
        nrec=mycursor.rowcount
        print('total records found are',nrec)
        print('%10s'%'Rollno','%10s'%'Name','%10s'%'Class','%10s'%'fee')
        print('_________________________________________________________')
        for row in mydata:
            print('%10s'%row[0],'%10s'%row[1],'%10s'%row[2],'%10s'%row[3])
            print('_________________________________________________________')

#exist
    else:
        print('_________________________________________________________')
        print('****************************EXIT*************************')
        print('_________________________________________________________')

student_info()
while True:
    ch=input('do you want to work more(y/n)')
    if ch=='y' or ch=='Y':
        student_info()
    else:
        break


        
        

        
        
 
        
        
            

    

    
    


