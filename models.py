from datetime import timedelta, datetime

from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Registration(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(50),nullable=False)
    password=db.Column(db.String(50),nullable=False)
    created_at=db.Column(db.DateTime,default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)