from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask.globals import request
from datetime import datetime

# import pymysql
# pymysql.install_as_MySQLdb()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codeworld'

db = SQLAlchemy(app)

# id , name,phone_num,msg,date,email
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    phone_num = db.Column(db.String(13), unique=True, nullable=False)
    msg = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.String(12),  nullable=True)
    email = db.Column(db.String(20), unique=True, nullable=False)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/post")
def post():
    return render_template('post.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact", methods = ['GET','POST'])
def contact():
    if(request.method=='POST'):
        
        
        name = request.form.get('name');
        email = request.form.get('email');
        phone = request.form.get('phone_num');
        message = request.form.get('message');
        
        entry=Contact(name=name,phone_num=phone,msg=message, date=datetime.now() ,email=email);
        db.session.add(entry)
        db.session.commit()
        
    
    # db.session.add()
    # db.session.commit()
    return render_template('contact.html')

app.run(debug=True)