S='''
     1.Credit
     2.Debit
     3.Mini_Statement
     4.Exit
'''

name="sankar"
password="123"
user_name=input("Enter the user Name: ")
passwords=input("Enter the user password: ")
Amount=10000
if name==user_name and passwords==password:
    
    while True:
        print(S)
        option=int(input("Enter the Option:"))
        if option==1:
            credit_amount=float(input("Enter the amount: "))    
            print("Amount after credit:",Amount+credit_amount)
        elif option==2:
            Debit_amount=float(input("Enter the amount: "))
            print("Amount after Debit:",Amount-Debit_amount)
            
        elif option==3:
            print("Amount in your account:",Amount)
        elif option==4:
            break
  
else:
    print("incorect")