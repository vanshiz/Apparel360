import mysql.connector as a
mydb = a.connect(host="localhost", user="root", passwd="",database="clothstore")
c=mydb.cursor()
c.execute( "use clothstore")
def adddata():
 print("""
\t\t\t\t\t\t***********************Entering Data ***********************
""")
 sno=int(input("Enter the serial no:"))
 r=input("Enter the reason for expenditure:")
 n=input("enter the reason no for expenditure:")
 a=int(input("Enter the amount paid:"))
 d=input("Enter date of expenditure(yyyy-mm-dd):")
 p=input("Is the amount paid(y/n):")
 f=input("Enter the floor number:")
 t=(sno,n,r,f,a,d,p)
 c=mydb.cursor()
 c.execute("insert into Rents_and_Expenditure values(%s,%s,%s,%s,%s,%s,%s)",t)
 mydb.commit()
 print("Data Entered Successfully")
def deletedata():
    print("""
    \t\t\t\t\t\t*********************** Deleting Data ***********************
    """)
    try:

        r=input("Enter the name of the entry to be deleted(Reason):")
        d=("Delete from Rents_and_Expenditure where Reason_no=%s")
        t=(r,)
        s=input("Are you sure you want to delete the entry (y/n):")
        if s=="y" or s=="Y":
            c.execute(d,t)
            mydb.commit()
            print("ENTRY DELETED")
        else:
            c.execute("Select * from Rents_and_Expenditure")
            result=c.fetchall()

    except:
        print("ERROR!! Entry not found")

def displaydata():
    print("""
    \t\t\t\t\t\t*********************** Displaying Data ***********************
    """)
    c.execute("select * from Rents_and_Expenditure")
    results=c.fetchall()
    for x in results:
        print(x)


def updatedata():
    print("""
    \t\t\t\t\t\t*********************** Updating Data ***********************
    """)
    ca="y"
    while(ca=="y"):
        ch=int(input("""Enter the thing you wish to change
        1. Reason
        2. Floor no.
        3. Amount
        4. Date
        5. Paid
        6. Exit
        """))
        if ch==1:
            print("""
            \t\t\t\t\t\t\t\t-------------------UPDATING REASON ---------------------
            """)

            R=input("Enter the reason to be changed:")
            rno=input("Enter the reason no in which you want to change the reason;")
            q=("Update rents_and_expenditure set reason=%s where reason_no=%s")
            data=(R,rno)
        elif ch==2:
            print("""
            \t\t\t\t\t\t\t\t--------------------UPDATING FLOOR NO--------------------
            """)
            fno=input("Enter the floor number which you want to change:")
            rno=input("Enter the reason no in which you want to change the reason;")
            q=("Update rents_and_expenditure set floor_no=%s where reason_no=%s")
            data=(fno,rno)


        elif ch==3:
            print("""
            \t\t\t\t\t\t\t\t-------------------UPDATING AMOUNT---------------------
            """)
            amt=input("Enter the amount which you want to change:")
            rno=input("Enter the reason no in which you want to change the reason;")
            q=("Update rents_and_expenditure set amount=%s where reason_no=%s")
            data=(amt,rno)
        elif ch==4:
            print("""
            \t\t\t\t\t\t\t\t-------------------UPDATING DATE---------------------
            """)
            d=input("Enter the date which you want to change:")
            rno=input("Enter the reason no in which you want to change the reason;")
            q=("Update rents_and_expenditure set date=%s where reason_no=%s")
            data=(d,rno)
        elif ch==5:
            print("""
            \t\t\t\t\t\t\t\t-------------------UPDATING PAID---------------------
            """)
            p=input("Status of payment(y/n):")
            rno=input("Enter the reason no in which you want to change the reason;")
            q=("Update rents_and_expenditure set paid=%s where reason_no=%s")
            data=(p,rno)
        elif ch==6:
            print("""
            \t\t\t\t\t\t\t\t############### Exiting UPDATE #################
            """)
            break
            c.execute(q,data)
            mydb.commit()
            print("Changes are done!")
def Rents_and_expenditures():
    c='y'
    while(c=='y'):
        print("""\t\t....................................THIS SECTION IS BUILD FOR WORKING IN THE FIELD OF RENTS &
        EXPENDITURES..................................
         \t\t----------------------------------- TASKS -------------------------------------------------
        """)
        print("\t\t\t\t\t\t\t\t1. Add Record in Rents and expenditure.")
        print("\t\t\t\t\t\t\t\t2. Update a record in Rents and expenditure." )
        print("\t\t\t\t\t\t\t\t3. To delete a record in Rents and expenditure.")
        print("\t\t\t\t\t\t\t\t4. To display the records of Rents and expenditure.")
        print("\t\t\t\t\t\t\t\t5. Exit")
        choice=int(input("Enter the choice of your:"))
        if choice==1:
            adddata()
        elif choice==2:
            updatedata()
        elif choice==3:
            deletedata()
        elif choice==4:
            displaydata()
        elif choice==5:
            print("""
            \t\t\t\t\t\t\t\t################# Exiting #################""")
            break
        else:
            print("""||REQUEST DENIED||
            INVALID CHOICE...""")


import mysql.connector as a
mydb = a.connect(host="localhost", user="root", passwd="",database="clothstore")
c=mydb.cursor()
c.execute("use clothstore")
def padddata():
    print("""
    \t\t\t\t\t\t*********************** Entering Data ***********************
    """)
    sno=int(input("Enter the serial code:"))
    x=int(input("Enter HSN code:"))
    y=input("Enter the name of the PURCHASE:")
    z=input("Enter the company:")
    d=int(input("Enter the quantity:"))
    p=int(input("Enter cost per item:"))
    q=input("enter the date:")
    t=(sno,x,y,z,d,p,q)
    c=mydb.cursor()
    c.execute("insert into PURCHASE values(%s,%s,%s,%s,%s,%s,%s)",t)
    mydb.commit()
    print("Data Entered Successfully")
def pdeletedata():
    print("""
    \t\t\t\t\t\t*********************** Deleting Data ***********************
    """)
    try:
        r=input("Enter the HSN_CODE:")
        d=("Delete from PURCHASE where HSN_code=%s")
        t=(r,)
        s=input("Are you sure you want to delete the entry (y/n):")
        if s=="y" or s=="Y":
            c.execute(d,t)
            mydb.commit()
            print("ENTRY DELETED")
        else:
            c.execute("Select * from purchase")
            result=c.fetchall()
    except:
        print("ERROR!! Entry codet found")
def pdisplaydata():
    print("""
    \t\t\t\t\t\t*********************** Displaying Data ***********************
    """)
    c.execute("select * from purchase order by s_no")
    results=c.fetchall()
    for x in results:
        print(x)
def pupdatedata():
    print("""
    \t\t\t\t\t\t*********************** Updating Data ***********************
    """)
    ca="y"
    while(ca=="y"):
        ch=int(input("""Enter the thing you wish to change
        1. Item_name
        2. Brand
        3. Quantity
        4. cost_per_item
        5. Purchase_Date
        6. Exit
        """))
        if ch==1:
            print("""
            \t\t\t\t\t\t-------------------UPDATING Item_name---------------------
            """)

            R=input("Enter the cloth name:")
            rcode=input("Enter the HSN code in which you want to change ;")
            q=("Update purchase set item_name=%s where HSN_code=%s")
            data=(R,rcode)


        elif ch==2:
            print("""
            \t\t\t\t\t\t-------------------UPDATING BRAND---------------------
            """)
            amt=input("Enter the brand:")
            rcode=input("Enter the HSN code in which you want to change ;")
            q=("Update purchase set company=%s where HSN_code=%s")
            data=(amt,rcode)
        elif ch==3:
            print("""
            \t\t\t\t\t\t-------------------UPDATING QUANTITY---------------------
            """)
            d=input("Enter the quantity:")
            rcode=input("Enter the HSN code in which you want to change ;")
            q=("Update purchase set quantity=%s where HSN_code=%s")
            data=(d,rcode)
        elif ch==4:
            print("""
            \t\t\t\t\t\t-------------------UPDATING COST_PER_ITEM---------------------
            """)
            p=input("Enter the cost_per_item:")
            rcode=input("Enter the HSN code in which you want to change;")
            q=("Update purchase set costprice_peritem=%s where HSN_code=%s")
            data=(p,rcode)
        elif ch==5:
            print("""
            \t\t\t\t\t\t-------------------UPDATING Purchase_date---------------------
            """)
            p=input("Enter the purchase date:")
            rcode=input("Enter the HSN code in which you want to change;")
            q=("Update purchase set purchase_date=%s where HSN_code=%s")
            data=(p,rcode)
        elif ch==6:
            print("""
            \t\t\t\t\t\t############### Exiting UPDATE #################
            """)
            break
            c.execute(q,data)
            mydb.commit()
            print("Changes are done!")
def purchase():
    c='y'
    while(c=='y'):
        print("""....................................THIS SECTION IS BUILD FOR WORKING IN THE FIELD OF
        PURCHASE..................................
        ----------------------------------- TASKS -------------------------------------------------
        """)
        print("\t\t\t\t\t\t\t\t1. Add Record in purchase.")
        print("\t\t\t\t\t\t\t\t2. Update a record in purchase." )
        print("\t\t\t\t\t\t\t\t3. To delete a record in purchase.")
        print("\t\t\t\t\t\t\t\t4. To display the records of purchase.")
        print("\t\t\t\t\t\t\t\t5. Exit")
        choice=int(input("Enter the choice of your:"))
        if choice==1:
            padddata()
        elif choice==2:
            pupdatedata()
        elif choice==3:
            pdeletedata()
        elif choice==4:
            pdisplaydata()
        elif choice==5:
            print("""
            \t\t\t\t\t\t################# Exiting #################""")
            break
        else:
            print("""||REQUEST DENIED||
            INVALID CHOICE...""")
#Sales
import mysql.connector as a
mydb = a.connect(host="localhost", user="root", passwd="",database="clothstore")
c=mydb.cursor()
c.execute( "use clothstore")
def sadddata():
    print("""
    \t\t\t\t\t\t*********************** Entering Data ***********************
    """)
    sno=int(input("Enter the serial code:"))
    x=int(input("Enter HSN code:"))
    y=input("Enter the name of the sale:")
    d=int(input("Enter the quantity:"))
    p=int(input("Enter cost per item:"))
    q=int(input("Enter the total amount:"))
    r=input("enter the sale_date:")
    t=(sno,x,y,d,p,q,r)
    c=mydb.cursor()
    c.execute("insert into sale values(%s,%s,%s,%s,%s,%s,%s)",t)
    mydb.commit()
    print("Data Entered Successfully")
def sdeletedata():
    print("""
    \t\t\t\t\t\t*********************** Deleting Data ***********************
    """)
    try:

        r=input("Enter the HSN_code:")
        d=("Delete from sale where HSN_code=%s")
        t=(r,)
        s=input("Are you sure you want to delete the entry (y/n):")
        if s=="y" or s=="Y":
            c.execute(d,t)
            mydb.commit()
            print("ENTRY DELETED")
        else:
            c.execute("Select * from sale")
            result=c.fetchall()
    except:
        print("ERROR!! Entry not found")

def sdisplaydata():
    print("""
    \t\t\t\t\t\t*********************** Displaying Data ***********************
    """)
    c.execute("select * from sale order by S_no")
    results=c.fetchall()
    for x in results:
        print(x)
def supdatedata():
    print("""
    \t\t\t\t\t\t*********************** Updating Data ***********************
    """)
    ca="y"
    while(ca=="y"):
        ch=int(input("""Enter the thing you wish to change
        1. Item_name
        2. Total amount
        3. Quantity
        4. cost_per_item
        5. Sale_Date
        6. Exit
        """))
        if ch==1:
            print("""
            \t\t\t\t\t\t-------------------UPDATING Item_name---------------------
            """)

            R=input("Enter the cloth name:")
            rcode=input("Enter the HSN code in which you want to change ;")
            q=("Update sale set item_name=%s where HSN_code=%s")
            data=(R,rcode)


        elif ch==2:
            print("""
            \t\t\t\t\t\t-------------------UPDATING Total amount---------------------
            """)
            amt=int(input("Enter the amount:"))
            rcode=input("Enter the HSN code in which you want to change ;")
            q=("Update sale set total_amount=%s where HSN_code=%s")
            data=(amt,rcode)
        elif ch==3:
            print("""
            \t\t\t\t\t\t-------------------UPDATING QUANTITY---------------------
            """)
            d=input("Enter the quantity:")
            rcode=input("Enter the HSN code in which you want to change ;")
            q=("Update sale set quantity=%s where HSN_code=%s")
            data=(d,rcode)
        elif ch==4:
            print("""
            \t\t\t\t\t\t-------------------UPDATING COST_PER_ITEM---------------------
            """)
            p=input("Enter the cost_per_item:")
            rcode=input("Enter the HSN code in which you want to change;")
            q=("Update sale set Netcost_peritem=%s where HSN_code=%s")
            data=(p,rcode)
        elif ch==5:
            print("""
            \t\t\t\t\t\t-------------------UPDATING sale_date---------------------
            """)
            p=input("Enter the sale date:")
            rcode=input("Enter the HSN code in which you want to change;")
            q=("Update sale set sale_date=%s where HSN_code=%s")
            data=(p,rcode)
        elif ch==6:
            print("""
            \t\t\t\t\t\t############### Exiting UPDATE #################
            """)
            break
            c.execute(q,data)
            mydb.commit()
            print("Changes are done!")
def sales():
    c='y'
    while(c=='y'):
        print("""\t\t....................................THIS SECTION IS BUILD FOR WORKING IN THE FIELD OF
        PURCHASE..................................
        \t\t----------------------------------- TASKS -------------------------------------------------
        """)
        print("\t\t\t\t\t\t\t\t1. Add Record in sales.")
        print("\t\t\t\t\t\t\t\t2. Update a record in sales." )
        print("\t\t\t\t\t\t\t\t3. To delete a record in sales.")
        print("\t\t\t\t\t\t\t\t4. To display the records of sales.")
        print("\t\t\t\t\t\t\t\t5. Exit")
        choice=int(input("Enter the choice of your:"))
        if choice==1:
            sadddata()
        elif choice==2:
            supdatedata()
        elif choice==3:
            sdeletedata()
        elif choice==4:
            sdisplaydata()
        elif choice==5:
            print("""
            \t\t\t\t\t\t\t\t################# Exiting #################""")
            break
        else:
            print("""||REQUEST DENIED||
            INVALID CHOICE...""")
#CLOTH
import mysql.connector as a
mydb = a.connect(host="localhost", user="root", passwd="",database="clothstore")
c=mydb.cursor()
c.execute( "use clothstore")
def cadddata():
    print("""
    \t\t\t\t\t\t*********************** Entering Data ***********************
    """)
    sno=int(input("Enter the serial no:"))
    x=int(input("Enter HSN code:"))
    y=input("Enter the name of the cloth:")
    z=input("Enter the brand:")
    d=int(input("Enter the quantity:"))
    p=int(input("Enter cost per item:"))
    t=(sno,x,y,z,d,p)
    c=mydb.cursor()
    c.execute("insert into cloth values(%s,%s,%s,%s,%s,%s)",t)
    mydb.commit()
    print("Data Entered Successfully")
def cdeletedata():
    print("""
    \t\t\t\t\t\t*********************** Deleting Data ***********************
    """)
    try:
        r=input("Enter the cloth name:")
        d=("Delete from cloth where cloth=%s")
        t=(r,)
        s=input("Are you sure you want to delete the entry (y/n):")
        if s=="y" or s=="Y":
            c.execute(d,t)
            mydb.commit()
            print("ENTRY DELETED")
        else:
            c.execute("Select * from cloth")
            result=c.fetchall()
    except:
            print("ERROR!! Entry not found")
def cdisplaydata():
    print("""
    \t\t\t\t\t\t*********************** Displaying Data ***********************
    """)
    c.execute("select * from cloth")
    results=c.fetchall()
    for x in results:
        print(x)
def cupdatedata():
    print("""
    \t\t\t\t\t\t*********************** Updating Data ***********************
    """)
    ca="y"
    while(ca=="y"):
        ch=int(input("""Enter the thing you wish to change
        1. cloth
        2. brand
        3. quantity
        4. cost_per_item
        5. Exit
        """))
        if ch==1:
            print("""
            \t\t\t\t\t\t-------------------UPDATING CLOTH---------------------
            """)

            R=input("Enter the cloth name:")
            rno=input("Enter the HSN no in which you want to change ;")
            q=("Update CLOTH set CLOTH=%s where HSN_CODE=%s")
            data=(R,rno)


        elif ch==2:
            print("""
            \t\t\t\t\t\t-------------------UPDATING BRAND---------------------
            """)
            amt=input("Enter the brand:")
            rno=input("Enter the HSN no in which you want to change ;")
            q=("Update CLOTH set brand=%s where HSN_CODE=%s")
            data=(amt,rno)
        elif ch==3:
            print("""
            \t\t\t\t\t\t-------------------UPDATING QUANTITY---------------------
            """)
            d=input("Enter the quantity:")
            rno=input("Enter the HSN no in which you want to change ;")
            q=("Update CLOTH set quantity=%s where HSN_CODE=%s")
            data=(d,rno)
        elif ch==4:
            print("""
            \t\t\t\t\t\t-------------------UPDATING COST_PER_ITEM---------------------
            """)
            p=input("Enter the cost_per_item:")
            rno=input("Enter the HSN no in which you want to change;")
            q=("Update CLOTH set cost_peritem=%s where HSN_CODE=%s")
            data=(p,rno)
        elif ch==5:
            print("""
            \t\t\t\t\t\t############### Exiting UPDATE #################
            """)
            break
            c.execute(q,data)
            mydb.commit()
            print("Changes are done!")
def cloth():
    c='y'
    while(c=='y'):
        print("""\t\t....................................THIS SECTION IS BUILD FOR WORKING IN THE FIELD OF
        CLOTH..................................
        \t\t----------------------------------- TASKS -------------------------------------------------
        """)
        print("\t\t\t\t\t\t\t\t1) Add Record in cloth.")
        print("\t\t\t\t\t\t\t\t2) Update a record in cloth." )
        print("\t\t\t\t\t\t\t\t3) To delete a record in cloth.")
        print("\t\t\t\t\t\t\t\t4) To display the records of cloth.")
        print("\t\t\t\t\t\t\t\t5) Exit")
        choice=int(input("Enter the choice of your:"))
        if choice==1:
            cadddata()
        elif choice==2:
            cupdatedata()
        elif choice==3:
            cdeletedata()
        elif choice==4:
            cdisplaydata()
        elif choice==5:
            print("""
            \t\t\t\t\t\t###################### Exiting ######################""")
            break
        else:
            print("""||REQUEST DENIED||
            INVALID CHOICE...""")
def adminlogin():
    print(">>>>>>>>>>>>>>>>>WELCOME TO APPAREL 360 CLOTHING STORE<<<<<<<<<<<<<<<<<<<<")
    print("..................THIS SYSTEM ALLOWS YOU TO PERFORM THE FOLLOWING TASKS!!...................... ")
    print("TASKS")
    print("1) CLOTHES INVENTORY")
    print("2) TRANSACTIONS")
    print("3) RENTS AND EXPENDITURE")
    print("4) Exit")
    v=int(input("Enter your preference:"))
    if v==1:
        cloth()
    elif v==2:
        print("THIS OPTION PROVIDES THE FOLLOWING FUNCTIONS---")
        print("1) Sales")
        print("2) Purchase")
        w=input("Enter the choice:")
        if w=="1":
            sales()
        elif w=="2":
            purchase()
        else:
            print("INVALID OPTION")
    elif v==3:
        Rents_and_expenditures()
    elif v==4:
        print("Exiting! Thank you for visiting us!")
    else:
        print("INVALID CHOICE!")

#LOGIN
print(">>>>>>>>>>>>>>>>>>>>>>>>>>...LOGIN CREDENTIALS...<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
user=input("Enter username:")
pswd=input("Enter the password:")
if user=="A":
    if pswd=="1":
        print("ACCESS GRANTED")
        adminlogin()
    else:
        print("INVALID PASSWORD")
        print("||ACCESS DENIED||")
else:
 print("INVALID USERNAME!!")