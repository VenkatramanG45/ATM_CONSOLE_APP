from ATM_DB import DBHelper
from mysql import connector
from history import History

class Bank:
    

    def Print_Menu(self):
        print("*********WELCOME**********")
        print()
        print("PRESS 1 to Open account")
        print("PRESS 2 to display last Transaction")
        print("PRESS 3 to deposit")
        print("PRESS 4 to withdraw")
        print("PRESS 5 to exit program")
        print("PRESS 6 to check balence")
        print("PRESS 7 to View Full History")
        print("PRESS 8 to Remove Account")
        print()

    def GetInput(self):
        self.userid=int(input("Enter user id:"))
        self.username=input("Enter the Name:")
        self.phone=input("Enter user Phone:")
        self.dob=input("Enter date of birth :")
        self.pin=int(input("Enter pin : "))
        db.insert_user(self.userid,self.username,self.phone,self.dob,self.pin)


    def Get_Choice(self):
        
        while True:
            try:
                choice=int(input())
                if choice==1:
                    self.GetInput()
        
                elif choice==2:
                    #Display User
                    db.fetch_all()
                elif choice==3:
                    res=db.UserID()
                    #print(res)
                    pin=int(input("Enter Id : "))
                    if pin in res:
                        db.Deposit(pin)
                    else:
                        print("Invalid ID")
                elif choice==4:
                    res=db.UserID()
                    pin=int(input("Enter Id : "))
                    if pin in res:
                        db.Withdraw(pin)
                    else:
                        print("Invalid ID")
                elif choice==5:
                    break

                elif choice==6:
                    pin=int(input("Enter the Pin : "))
                    print(db.fetch_Balence(pin))

                elif choice==7:
                    pin=int(input("Enter the pin : "))
                    h.ViewHistory()
                else:
                    print("Invlid Input ! Try again ")
            except Exception as e:
                print(e)
                print("Invalid Details ! Try again")

db=DBHelper()
h=History()
h.Details()
#h.ALTER()
h.DropTrigInsertion()
h.DropTrigUpdation()
h.TrigInsert()
h.TrigUpdate()
#h.CreateView() 


def main():
    bank=Bank()
    bank.Print_Menu()
    bank.Get_Choice()

if __name__=="__main__":
    main()

