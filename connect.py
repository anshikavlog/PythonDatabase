import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',database='mmmutdb',password='',charset='utf8')
cursor=mydb.cursor()
print("Connection established")