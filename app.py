from flask import *
# , redirect, render_template, url_for, request
from DB_handler import DBmodule


app = Flask(__name__)
DB = DBmodule()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/list")
def post_list():
    pass

@app.route("/post/<int>")
def post():
    pass

@app.route("/login")
def login():
    pass

@app.route("/login_done")
def login_done():
    pass

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/signin_done")
def signin_done():
    pass

@app.route("/user/<uid>")
def user(uid):
    pass

@app.route("/write")
def write():
    pass

@app.route("/write_done",methods=["GET"])
def write_done():
    pass

if __name__ == '__main__':
    app.run(host="127.0.0.1",
            port="5000",
            debug=True)