from flask import Flask,render_template,request,make_response
import pymysql as sql
from flask import session


app = Flask(__name__)
app.secret_key = "iji1234doioddhooifohffofiejipjpoo"

@app.route('/')
def index():
    return render_template("nav.html")
    #return "hello world"

@app.route("/home/<name>/")
def home(name):
    return render_template("abc.html",n=name)
    #return "<h2 style='color:coral'>Welcome to my home</h2>"

@app.route("/<name>/<int:age>")
def vote(name,age):
    return render_template("abc.html",n=name,a=age)

@app.route("/home/<subject>/<int:m1>/<int:m2>/<int:m3>/")
def s(subject,m1,m2,m3):
    data = {
        'subject' : subject,
        'maths' : m1,
        'science' : m2,
        'english' : m3
    }
    return render_template("abc.html",data=data)
    #return "<h1 style='color:blue'> {} has average marks {}</h1>".format(subject,(m1+m2+m3)/3)

@app.route('/login/')
def login():
    if request.cookies.get('email'):
        return render_template("abc.html")
    return render_template("login.html")

@app.route('/login1/',methods=['GET','POST'])
def login1():
    email = request.form.get('email')
    password = request.form.get('pswd')
    try:
        db = sql.connect(host="localhost",port=3306,user="root",password="",database="batch415")
    except Exception as e:
        return f"{e}"
    else:
        c = db.cursor()
        c.execute("select * from users where email='{}'".format(email))
        data = c.fetchone()
        if data[2] == password:
            session['email'] = email
            session['islogin'] = 'true'
            return render_template("abc.html")
            #resp = make_response(render_template("abc.html"))
            #resp.set_cookie('email',email)
            #resp.set_cookie('islogin','true')
            #return resp
            #return f"{email} and {password}"
        else:
            error = "Invalid Password"
            return render_template("login.html",error=error)

@app.route("/signup/")
def signup():
    return render_template("signup.html")

@app.route('/signup1/',methods=['GET','POST'])
def signup1():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('pswd')
    gender = request.form.get('gender')
    pic = request.form.get('myfile')
    f = request.files['myfile']
    file = f.filename
    print(file)
    f.save('static/images/'+file)
    try:
        db = sql.connect(host="localhost",port=3306,user="root",password="",database="batch415")
    except Exception as e:
        return f"{e}"
    else:
        c = db.cursor()
        c.execute("select * from users where email='{}'".format(email))
        data = c.fetchone()
        if data:
            error = "User already registered"
            return render_template("signup.html",error=error)
        else:
            #c.execute("insert into users values('{}','{}','{}','{}','{}')".format(name,email,password,gender,pic))
            #db.commit()
            error = "User added successfully"
            return render_template("login.html",error=error)
    
    return f"{name} and {gender}"

@app.route('/logout/')
def logout():
    #resp = make_response(render_template("login.html"))
    #resp.delete_cookie('email')
    #resp.delete_cookie('islogin')
    #return resp
    del session['email']
    del session['islogin']
    return render_template("login.html")

app.run(host="localhost",port=80,debug=True)
