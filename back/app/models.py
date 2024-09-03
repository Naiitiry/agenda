from datetime import datetime, timedelta
from sqlalchemy.sql import func
from flask_login import UserMixin
from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model, UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(150),nullable=False,unique=True)
    email=db.Column(db.String(150),nullable=False,unique=True)
    password_hash=db.Column(db.String(300),nullable=False)
    tasks=db.relationship('Task',backref='user',lazy=True)

    def set_password(self,password):
        self.password_hash=generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
    
class Task(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(150),nullable=False)
    description=db.Column(db.Text,nullable=True)
    creation_date=db.Column(db.DateTime,nullable=False,default=func.now)
    deadline=db.Column(db.DateTime,nullable=False)
    completed=db.Column(db.Boolean,default=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def time_left(self):
        return self.deadline - func.now()
    
    def overdue(self):
        return func.now()>self.deadline
    
    def extend_deadline(self,days):
        self.deadline += timedelta(days=days)