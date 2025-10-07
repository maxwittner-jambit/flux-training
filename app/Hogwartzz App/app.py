from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

usr=os.environ.get('POSTGRES_USER')
pw=os.environ.get('POSTGRES_PASSWORD')
host=os.environ.get('POSTGRES_HOST')
database=os.environ.get('POSTGRES_DB')

uri=f'postgresql://{usr}:{pw}@{host}/{database}'
app.config['SQLALCHEMY_DATABASE_URI']=uri

db=SQLAlchemy(app)


class Student(db.Model):
    __tablename__='students'
    id=db.Column(db.Integer,primary_key=True)
    fname=db.Column(db.String(40))
    lname=db.Column(db.String(40))
    pet=db.Column(db.String(40))

    def __init__(self,fname,lname,pet):
        self.fname=fname
        self.lname=lname
        self.pet=pet

with app.app_context():
    # Create the tables
    db.create_all()


@app.route('/')
def index():
    try:
        page= request.args.get('page',1,type=int)
        all_students = Student.query.order_by(-(Student.id)).paginate(page=page,per_page=3)
        return render_template('index.html', students=all_students)
    except Exception as e:
        return render_template('error.html', error=e)

@app.route('/submit', methods=['POST'])
def submit():
    fname= request.form['fname']
    lname=request.form['lname']
    pet=request.form['pets']

    student=Student(fname,lname,pet)
    db.session.add(student)
    db.session.commit()

    #fetch a certain student2
    studentResult=db.session.query(Student).filter(Student.id==1)
    for result in studentResult:
        print(result.fname)

    return render_template('success.html', data=fname)


if __name__ == '__main__':  #python interpreter assigns "__main__" to the file you run
    app.run(host="0.0.0.0",port=5000,debug=True)