from flask import Flask                         # From the flask package import the Flask class

app = Flask(__name__)                           # Instantiat the Flask class into app (which is now an obj)
# the double __ is called a magic variable or dunder variable

@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

@app.route("/about")
def about_me():
    me = {
        "first_name": "Kevin",
        "last_name": "Cruz",
        "hobbies": "Coding",
        "active": True
    }
    return me