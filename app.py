from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Secret Key"

#SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



#Creating model table for our CRUD database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    DOB = db.Column(db.String(100))
    amount_due = db.Column(db.String(100))


    def __init__(self,id, firstname, lastname, DOB, amount_due):

        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.DOB = DOB
        self.amount_due = amount_due


@app.route('/')
def Index():
    all_data = Data.query.all()

    return render_template("index.html", employees = all_data)



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':
        id = request.form['id']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        DOB = request.form['DOB']
        amount_due = request.form['amount_due']


        my_data = Data(id,firstname, lastname, DOB, amount_due)
        db.session.add(my_data)
        db.session.commit()

        

        return redirect(url_for('Index'))


@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))
        
        
        my_data.firstname = request.form['firstname']
        my_data.lastname = request.form['lastname']
        my_data.DOB = request.form['DOB']
        my_data.amount = request.form['amount_due']

        db.session.commit()
        

        return redirect(url_for('Index'))

@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    return redirect(url_for('Index'))






if __name__ == "__main__":
    app.run(debug=True)