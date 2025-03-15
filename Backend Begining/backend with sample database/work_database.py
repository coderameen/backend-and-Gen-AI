#CRUD: Create, Read, Update, delete
import sqlite3

#create db and connect it
conn = sqlite3.connect("mydb.db")
if conn:
    print("db created and connected successfully!")
else:
    print("failed to create and connect!!")


#create cursor to execute queries
cursor = conn.cursor()



#create tables
cursor.execute("""CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER)""")
conn.commit()
print("Table has created successfully")



# #insert dummy values to table
# cursor.execute("""INSERT INTO user(name,age) VALUES(?,?)""",("Sanaan",30))
# cursor.execute("""INSERT INTO user(name,age) VALUES(?,?)""",("Prajwal",50))
# conn.commit()
# print("Data inserted successfully!!")


#Read/Retreive Data
cursor.execute("""SELECT * FROM user""")
rows = cursor.fetchall()

# print(rows)
for row in rows:
    # print(row)
    print(row[1])
    
    
#Update data
cursor.execute("""UPDATE user SET name=? WHERE id=?""",("Mohammed Sanaan",1))
conn.commit()
print("updated successfulyy")


#Delete data
cursor.execute("""DELETE FROM user WHERE name=?""",('Prajwal',))
conn.commit()
print("data deleted successfuly")

#Delete table
cursor.execute("""DROP TABLE user""")
conn.commit()
print("table deleted successfully")