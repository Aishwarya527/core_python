import mysql.connector as c
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234", 
    database="cvr"
)
mycursor = mydb.cursor()

# Insert 5 rows into the departments table
# mycursor.execute("""
#     INSERT INTO department1 (department_name, manager_id, location, budget)
#     VALUES
#     ('CSE', 101, 'BlockA', 50000.00),
#     ('DS', 102, 'BlockB', 30000.00),
#     ('AIML', 103, 'BlockC', 60000.00),
#     ('CS', 104, 'BlockD', 45000.00),
#     ('Civil', 105, 'BlockE', 70000.00)
#  """)


#delete department details
# mycursor.execute("DELETE FROM department1 WHERE manager_id = 101")

#Update department name
#mycursor.execute("update department1 set department_name='Mech' where manager_id=102")

#display department table
# mycursor.execute("select * from department1")
# depts=mycursor.fetchall()
# for dpt in depts:
#     print(dpt)

#displaying the department details using order by the department name in ascending order
# mycursor.execute("select * from department1 order by department_name asc")
# depts=mycursor.fetchall()
# for dpt in depts:
#     print(dpt)

#displaying the department details whose budget between 50000 to 70000
# mycursor.execute("select * from department1 where budget between 50000 and 70000")
# depts=mycursor.fetchall()
# for dpt in depts:
#     print(dpt)

#displaying the department details whose location is same i.e, BlockE
mycursor.execute("select * from department1 where location='BlockE'")
depts=mycursor.fetchall()
for dpt in depts:
    print(dpt)
    
# Commit the changes to save the data
mydb.commit()



