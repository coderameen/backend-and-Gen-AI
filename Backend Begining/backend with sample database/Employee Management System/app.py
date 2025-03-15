from flask import Flask, render_template, redirect, url_for, request
from database import conn, cursor

app = Flask(__name__)


#GET API: default route(login page)
@app.route("/")
def login():
    return render_template("login.html")

@app.route("/logindb", methods=['GET','POST'])
def logindb():
    if request.method == 'POST':
        # breakpoint()
        username = request.form['usrbox']
        password = request.form['pwdbox']
        
        #Check if its an valid usernaem(check in db)
        cursor.execute("""SELECT username FROM register""")
        rows = cursor.fetchall()
        # print(rows)#[["prajwal"],["sanaan"]]
        alluser = []
        for user in rows:
            alluser.append(user[0])
            
        # print(alluser)#['prajwal', 'sanaan']
        
        if username in alluser:
            #fetch password for that user
            cursor.execute("""SELECT password FROM register WHERE username=?""",(username,))
            db_pwd = cursor.fetchone()
            db_pwd = db_pwd[0] #'prajwal'
            if db_pwd == password:
                return redirect(url_for('home'))
            else:
                return "Invalid Passowrd"
            
        else:
            return "Invalid Username! username doesn't exists"
    


@app.route("/signup")
def signup():
    return render_template("signup.html")

#add signup data in dabase 
@app.route("/regdb", methods=['GET','POST'])
def regdb():
    if request.method == 'POST':
        username = request.form['usrbox']
        password1 = request.form['pwdbox']
        password2 = request.form['repwdbox']
        # print([username, password1,password2])
        # return [username, password1,password2]
        if password1 == password2:
            #insert username and password in register table
            cursor.execute("""INSERT INTO register(username,password) VALUES(?,?)""",(username,password1))
            conn.commit()
            return "Registration Successfull"
        else:
            return "password dosen't matches!!"
        

@app.route("/ems_dashboard")
def home():
    return render_template("index.html")


@app.route("/addemp")
def addemp():
    return render_template("addemp.html")


@app.route("/addempdb", methods=['GET','POST'])
def addempdb():
    # breakpoint()
    if request.method == 'POST':
        empid = request.form['empidbox']
        empname = request.form['empnamebox']
        empdes = request.form['empdesbox']
        
        #insert into employees table
        cursor.execute("""INSERT INTO employees(emp_id, emp_name, emp_designation) VALUES(?,?,?)""",(empid,empname,empdes))
        conn.commit()
        return "Empoyee Added successfully!!"

        


if __name__=='__main__':
    app.run(debug=True)