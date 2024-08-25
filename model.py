from app import db


class Donor(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    name=db.Column(db.String(length=30), nullable=False)
    email=db.Column(db.String(length=30), nullable=False, unique=True)
    address=db.Column(db.String(length=100), nullable=False)