#!/usr/bin/python3

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    date_block = db.Column(db.String(50), nullable=False)
    cause = db.Column(db.String(50), nullable=False)
    host = db.Column(db.String(50), nullable=False)
    date_unblock = db.Column(db.String(50) , nullable=False)
    note = db.Column(db.String(50) , nullable=False)

    def __repr__(self):
        return f"User(name='{self.name}', date_block='{self.date_block}', cause='{self.cause}', host='{self.host}', date_unblock='{self.date_unblock}' , note ='{self.note}')"
