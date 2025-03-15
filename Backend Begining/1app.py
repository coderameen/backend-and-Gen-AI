#pip install flask
#from Package import Libraries
from flask import Flask

#step 2: initialize the app
app  = Flask(__name__)

#GET API
@app.route("/")
def home():
    return "sdfsdfdfsdfSanaan prajwal ameen mychangessssss!@!!"


#GET API: show the client information
@app.route("/clientinfo")
def clientinfo():
    return "MOI CISCO INTEL TAVANT"

#step 4: run the app
if __name__=='__main__':
    app.run(debug=True, port = 5001)#debug == True will keep track of your changes, no need to kill the server!


