import sqlite3
con=sqlite3.connect("employee.df")
print("database connected")
con.execute("create table emp_details(id int,name text,city text,salary int)")
print("table created")
con.execute("insert into emp_details(id,name,city,salary)values(1,'shyam','rajkot',50,000)")
con.execute("insert into emp_details(id,name,city,salary)values(2,'ravi','surat',25,000)")
con.execute("insert into emp_details(id,name,city,salary)values(3,'yash','rajkot',40,000)")
con.execute("insert into emp_details(id,name,city,salary)values(4,'princ','pune',45,000)")
con.execute("insert into emp_details(id,name,city,salary)values(5,'bhavy','gandhinagar',30,000)")
con.commit()
print("data insert successfully...")

con.execute("create table movie(name text,actor text,actress text,year int,director text)")

con.execute("insert into movie(name,actor,actress,year,director)values(ramlila,ranveersigh,deepika,2015,rohit shetty)")
con.execute("insert into movie(name,actor,actress,year,director)values(happy new year,sarukhan,deepika,2017,rohit shetty)")
con.commit()

data=con.execute("select * from movie")
for row in data:
    print('name',row[0])
    print('actor',row[1])
    print('actress',row[3])
    print('year',row[4])
    print('director',row[5])
con.commit()
