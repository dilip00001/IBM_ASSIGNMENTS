
from flask import *

act=Flask(__name__)

@act.route("/")
def homepage():
    return render_template("login.html")

@act.route("/user",methods=["POST","GET"])
def page():
    uname=request.form["username"]   
    uemail=request.form["email"]   
    unum=request.form["number"]   
    return render_template("index.html",name=uname,mailID=uemail,phonenumber=unum)

act.run(debug=True)


