#!/usr/bin/python3

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from models import db, User
from sqlalchemy.sql import text , or_

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
db.init_app(app)


with app.app_context():
    db.create_all()

@app.route('/')
def index():
    patients = User.query.all()
    return render_template('index.html', patients=patients)

@app.route('/add', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        date_block = request.form['date_block']
        cause = request.form['cause']
        host = request.form['host']
        date_unblock = request.form['date_unblock']
        note = request.form['note']
        patient = User(name=name, date_block=date_block, cause=cause, host=host, date_unblock=date_unblock , note = note )
        db.session.add(patient)
        db.session.commit()
        return redirect('/')
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_patient(id):
    patient = User.query.get_or_404(id)
    if request.method == 'POST':
        patient.name = request.form['name']
        patient.date_block = request.form['date_block']
        patient.cause = (request.form['cause'])
        patient.host = (request.form['host'])
        patient.date_unblock = request.form['date_unblock']
        patient.note = request.form['note']
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', patient=patient)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_patient(id):
    patient = User.query.get_or_404(id)
    db.session.delete(patient)
    db.session.commit()
    return redirect('/')

@app.route('/select' , methods=['GET','POST'])
def select_patient():

    if request.method == 'POST':
        sign  = "User." + request.form.get('sign')
        condition = request.form.get('condition')
        value = (request.form.get('value'))
        message = sign + condition + "'" + value + "'"
        patient = User.query.filter(text(message)).all()
#        patient = Patient.query.filter(Patient.age>3).all()
        print(patient)
        return render_template("index.html" , patients = patient)
    return render_template('select.html'  )


if __name__ == '__main__':
    app.run(debug=True)



