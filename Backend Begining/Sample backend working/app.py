from flask import Flask, render_template, request


app = Flask(__name__)
@app.route("/")
def home():
    #send data from backend to front end
    # result = [10,20,30,40,50,60]
    
    # result = ['Apple','Mango','Banana']
    
    result = [{'name':'sanaan','usn':'CS01'},{'name':'Prajwal','usn':'CSO2'}]
    return render_template("index.html", result = result)


@app.route("/add")
def add():
    return render_template("index2.html")


#POST API
@app.route("/adddata", methods=['GET','POST'])
def adddata():
    if request.method == 'POST':
        num1 = request.form['n1val']
        num2 = request.form['n2val']
        # return f"{num1} and {num2}"
        result = int(num1) + int(num2)
        return render_template("index2.html", result=result)

if __name__== '__main__':
    app.run(debug=True)