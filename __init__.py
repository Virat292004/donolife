from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(_name_)
app.config['SECRET_KEY'] = '3a08f1d98ca16819b3da55c92c7d26ad14fdd6314c122b93'
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///model.db"
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS']=False

db=SQLAlchemy(app)

from app import routes