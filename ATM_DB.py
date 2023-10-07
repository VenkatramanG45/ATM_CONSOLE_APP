from mysql import connector
#import datetime 
#import time
import pandas as pd


class DBHelper:
    def __init__(self):
        self.con=connector.connect(host='localhost',
                                   port='3306',  
                                   user='root',
                                   password='Venky#123$',
                                   database='My_bank')
        
        query='create table if not exists customer(userid int primary key,username varchar(200),phone varchar(12),dob varchar(12),pin int,balence int not null default 0,date varchar(15),time varchar(15),day varchar(15))'
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")
          

    #Insert
    def insert_user(self,userid,username,phone,dob,pin):
        
        query="insert ignore into customer(userid,username,phone,dob,pin)values('{}','{}','{}','{}','{}')".format(userid,username,phone,dob,pin)
       
        cur=self.con.cursor()
        self.Trig(cur)
        cur.execute(query)
        self.con.commit()  
        print("User save it to db")


    def inseret_Updation(self):
        query = "CREATE TRIGGER setdate_before_insert AFTER UPDATE ON customer FOR EACH ROW SET NEW.date = CURDATE(), NEW.time = curtime() , NEW.day = dayname(CURDATE())"
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        


    def DropTrig(self,cur):
        query="Drop Trigger if exists setdate_before_insert"
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()

    def Trig(self,cur):
        self.DropTrig(cur)
        query = "CREATE TRIGGER setdate_before_insert BEFORE INSERT ON customer FOR EACH ROW SET NEW.date = CURDATE(), NEW.time = curtime() , NEW.day = dayname(CURDATE())"
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        

    def fetch_all(self):
        query="select * from customer"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("User Id : ",row[0])
            print("User Name :",row[1])
            print("User Phone : ", row[2])
            print("Date of birth : ",row[3])
            print("PIN : ",row[4])
            print("Balence:",row[5])
            print("Date : ",row[6])
            print("Time: ",row[7])
            print("Day : ",row[8])
            print()
        
        '''db_cursor = self.con.cursor()
        db_cursor.execute('SELECT * FROM customer')

        table_rows = db_cursor.fetchall()

        df = pd.DataFrame(table_rows)'''

        #print(df)


    def fetch_Balence(self,pin):
        query="select balence from customer where pin={}".format(pin)
        cur=self.con.cursor()
        cur.execute(query)
        #self.con.commit()
        for i in cur:
            balence=i[0]
        #print(balence)
        return balence

        #print("Balence : ",balence )

    def DropTrig_Update(self,cur):
        query="Drop Trigger if exists set_before_update"
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
    

    def Update_Transaction(self,cur):
        self.DropTrig_Update(cur)
        query="CREATE TRIGGER set_before_update BEFORE UPDATE ON customer FOR EACH ROW SET NEW.date = CURDATE(), NEW.time = curtime() , NEW.day = dayname(CURDATE())"
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()     
        print("Updated")
        #self.trigger_updation()


    
    def Deposit(self,pin):
        res=self.fetch_Balence(pin)
        
        amt=int(input("Enter the amount to Deposit : "))
        bal=res+amt
        query="update customer  set balence={} where pin={}".format(bal,pin)
        cur=self.con.cursor()
        self.Update_Transaction(cur)
        cur.execute(query)
        self.con.commit()
        
        print("Amount Deposited...")
        #self.insert_user(userid,username,phone,dob,pin)
        


    def Withdraw(self,pin):
        res=self.fetch_Balence(pin)
        amt=int(input("Enter the amount to withdraw : "))    
        if amt<=res:
            
            bal=res-amt
            query="update customer  set balence={} where pin={}".format(bal,pin)
            cur=self.con.cursor()
            self.Update_Transaction(cur)
            cur.execute(query)
            self.con.commit()
            print("Amount Debited...")
           # self.insert_user(userid,username,phone,dob,pin)
            
        else:
            print("You cannot withdraw")
    

    def UserID(self):
        query="select pin from customer"
        cur=self.con.cursor()
        cur.execute(query)
        #self.con.commit()
        lst=[]
        lst2=[]
        for i in cur:
            lst.append(list(i))
        for i in lst:
            for j in i:
                lst2.append(j)
        return lst2
    


    
   
   
   