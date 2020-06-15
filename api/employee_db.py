import sqlite3  
  
con = sqlite3.connect("employee.db")  
print("Database opened successfully")  
#con.execute("drop table Employees")  

con.execute("create table Employees (id INTEGER PRIMARY KEY AUTOINCREMENT, fname TEXT NOT NULL, lname TEXT UNIQUE NOT NULL)")  
  
print("Table created successfully")  
  
con.close()  