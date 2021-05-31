# WAP in python to do basic operation in bank:
class Bank():
 def __init__(self,acno,name,bal):
  self.acno=acno
  self.name=name
  self.bal=bal
 def deposit(self,ac,amt):
  if(self.acno==ac):
   self.bal+=amt
   print("Your available balance is",self.bal,"in the account",self.acno)
  else:
   print("Enter valid account number")
 def withdraw(self,ac,amt):
  if(self.acno==ac):
   self.bal-=amt
   print("Your available balance is",self.bal,"in the account",self.acno)
  else:
   print("Enter valid account number")
 def Enquiry(self,ac):
  if(self.acno==ac):
   print("Your available balance is",self.bal,"in the account",self.acno)
  else:
   print("Enter valid account number")

account=int(input("Enter the account number"))
name=input("Enter your name")
amount=int(input("Enter the amount to be deposit"))
b=Bank(account,name,amount)
print("Your account is created")

ch=0
while ch!=4:
 print("1-->Deposit")
 print("2-->Withdraw")
 print("3-->Enquiry")
 print("4-->Exit")
 ch=int(input("Enter choice"))
 if(ch==1):
  a=int(input("Enter account number"))
  d=int(input("Enter amount to be deposited"))
  b.deposit(a,b)
 elif(ch==2):
  a=int(input("Enter account number"))
  d=int(input("Enter amount to be withdraw"))
  b.withdraw(a,d)
 elif(ch==3):
  a=int(input("Enter account number"))
  b.Enquiry(a)
 else:
  pass
 

