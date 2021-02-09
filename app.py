from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.secret_key = ""
  
#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/testingdb'
                                        #mysql+pymysql://username:passwd@host/databasename 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  
db = SQLAlchemy(app)

#Creating model table for our CRUD database
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))
  
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        db.create_all()
        
 #query on all our employee data
@app.route('/')
def Index():
    all_data = Employee.query.all()
    return render_template("index.html", employees = all_data)
db.create_all()



if __name__ == "__main__":
    app.run(debug=True)