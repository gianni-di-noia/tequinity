from flask_login import UserMixin

from . import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Receipt(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100))

    def store(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def load(cls, receipt_id):
        return cls.query.get(receipt_id)
