import mysql.connector
class Db:
 def connect(self):
  self.mydb=mysql.connector.connect(host='localhost',user='root',database='bankdb',password='',charset='utf8')
  self.cursor=self.mydb.cursor()
class Bank(Db):
 def create(self,acno,name,actype,balance):
  super().connect()
  query="insert into bankinfo values('"+acno+"','"+name+"','"+actype+"','"+str(balance)+"')"
  self.cursor.execute(query)
  self.mydb.commit()
  print("Your account is created")
 def deposit(self,acno,amt):
  query="select acno,balance from bankinfo where acno='"+acno+"'"
  super().connect()
  self.cursor.execute(query)
  result=self.cursor.fetchone()
  ano=result[0]
  balance=int(result[1])
  if(ano==result[0]):
   balance=balance+amt
   query="update bankinfo set balance='"+str(balance)+"' where acno='"+acno+"'"
   self.cursor.execute(query)
   self.mydb.commit()
   print("The amount",amt,"is credited in your account",acno)
  else:
   print("The account doesn't exist")
 def withdraw(self,acno,amt):
  query="select acno,balance from bankinfo where acno='"+acno+"'"
  super().connect()
  self.cursor.execute(query)
  result=self.cursor.fetchone()
  ano=result[0]
  balance=int(result[1])
  if(ano==result[0]):
   if(balance>=amt):
    balance=balance-amt
    query="update bankinfo set balance='"+str(balance)+"' where acno='"+acno+"'"
    self.cursor.execute(query)
    self.mydb.commit()
    print("The amount",amt,"is debited in your account",acno)
   else:
    print("Unsufficient Balance")
  else:
   print("The account doesn't exist")
 def viewbalance(self,acno):
  query="select acno,balance from bankinfo where acno='"+acno+"'"
  super().connect()
  self.cursor.execute(query)
  result=self.cursor.fetchone()
  ano=result[0]
  balance=int(result[1])
  if ano==result[0]:
   print("Balance amount is",balance,"in your account",acno)
  else:
   print("The account doesn't exist")

#TESTING
b=Bank()
ch=0
while ch!=5:
 print("1-->Create Account")
 print("2-->Deposit")
 print("3-->Withdraw")
 print("4-->View")
 print("5-->Exit")
 ch=int(input())
 if ch==1:
  acno=input("Enter account no: ")
  name=input("Enter name: ")
  actype=input("Enter account type: ")
  balance=int(input("Enter opening balance: "))
  b.create(acno,name,actype,balance)
 elif ch==2:
  acno=input("Enter account no: ")
  amt=int(input("Enter amount to be deposit"))
  b.deposit(acno,amt)
 elif ch==3:
  acno=input("Enter account no: ")
  amt=int(input("Enter amount to withdraw"))
  b.withdraw(acno,amt)
 elif ch==4:
  acno=input("Enter account no: ")
  b.viewbalance(acno)
 else:
  print("Invalid Choice")
   
 
  
 