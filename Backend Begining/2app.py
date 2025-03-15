from flask import Flask, redirect, url_for


app = Flask(__name__)

@app.route("/")
def login():
    return "This is my login page!!"


@app.route("/dashboard")
def dashboard():
    return "This is my dashboard"

@app.route("/user/<name>")#query params
def user(name):
    return f"Welcome  {name}"

@app.route("/logout")
def logout():
    return redirect(url_for("login"))


if __name__== '__main__':
    app.run(debug=True)