from flask import Flask, render_template,request
from Student import Student
from flask import session,g
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
data = dict()

@app.before_request
def before_request():
    g.user = None
    if 'data' in session:
        g.user = session['data']


@app.route("/")
def home():
    return render_template("Dashboard.html")


@app.route("/addProfile", methods=["GET","POST"])
def addprofile():
    name = request.form['studentName']
    roll_no = request.form['sRollNo']
    age = request.form['sAge']
    gender = request.form['gender']

    data = Student(name, roll_no, age, gender)
    return render_template("Dashboard.html", **locals(),rowTable=data)


@app.route("/updateProfile", methods=["GET","POST"])
def update():
    name = request.form['studentName']
    roll_no = request.form['rollNo']
    age = request.form['age']
    gender = request.form['gender']

    student = Student(name, roll_no, age, gender)
    return render_template("Dashboard.html", **locals())

@app.route("/delete", methods=["GET", "POST"])
def delete():
    print("dheeraj")


if __name__ == "__main__":
    app.run(debug=True)
