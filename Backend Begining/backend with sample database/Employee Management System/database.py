import sqlite3
conn = sqlite3.connect("companydb.db", check_same_thread=False)

if conn:
    print("Db created and connected succesfuly")
else:
    print("failed to connect")
    
    
#cursor: it is used to execute the query

cursor = conn.cursor()


#Create Employees table
cursor.execute("""CREATE TABLE IF NOT EXISTS employees(emp_id TEXT PRIMARY KEY NOT NULL, emp_name TEXT NOT NULL, emp_designation)""")
conn.commit()
print("table created successfuly")

cursor.execute("""CREATE TABLE IF NOT EXISTS register(username TEXT, password TEXT)""")
conn.commit()
print("register table created successfully")