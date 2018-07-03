# File for models/classes
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
class User(db.Model):
    """docstring for [object Object]."""
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
        @property
        def password(self):
            raise AttributeError('Failed You cannot read the password')
        @property.setter
        def password(self,password):
            self.pass_secure=generate_password_hash(password)
        def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)
class Stock_Info(db.Model):
    """docstring for [object Object]."""
    __tablename__='stocks_info'
    id=db.Column(db.Integer,primary_key=True)
    Name=db.Column(db.String(255))
    Company_id=db.Column(db.String(255))
    Security_id=db.Column(db.Integer)
    High_trade=db.Column(db.Integer)
    Low_trade=db.Column(db.Integer)
    Last_traded_price=db.Column(db.Integer)
    Close_price=db.Column(db.Integer)
    Prev_close=db.Column(db.Integer)
    Vol_traded=db.Column(db.Integer)
    Year_low_price=db.Column(db.Integer)
    Year_high_price=db.Column(db.Integer)
