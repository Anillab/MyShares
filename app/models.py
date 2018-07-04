# File for models/classes
from . import db
from werkzeug.security import generate_password_hash,check_password_hash

def saveobject(object):
    db.session.add(object)
    db.session.commit()

class STOCKSHistory(db.Model):
    __tablename__='stockshist'
    id=db.Column(db.Integer,primary_key=True)
    companyid = db.Column(db.BigInteger)
    json = db.Column(db.String(255350))
    def get_stocks(comapny):
        if STOCKSHistory.query.filter(companyid==comapny).first():
            return STOCKSHistory.query.filter(companyid==comapny).first()
        else:
            from .data import get_chart
            get_chart(comapny)
            return get_stocks(comapny)

class User(db.Model):
    """docstring for [object Object]."""
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(65535))
    email = db.Column(db.String(65535))
    phone_number=db.Column(db.BigInteger)
    pass_secure = db.Column(db.String(65535))
    @property
    def password(self):
        raise AttributeError('Failed You cannot read the password')
    @password.setter
    def password(self,password):
        self.pass_secure=generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

class Stock_Info(db.Model):
    """docstring for [object Object]."""
    __tablename__='stocks_info'
    id=db.Column(db.Integer,primary_key=True)
    Company_id=db.Column(db.String(65535))
    High_trade=db.Column(db.BigInteger)
    Low_trade=db.Column(db.BigInteger)
    Last_traded_price=db.Column(db.BigInteger)
    Close_price=db.Column(db.BigInteger)
    Prev_close=db.Column(db.BigInteger)
    Vol_traded=db.Column(db.BigInteger)
    Year_low_price=db.Column(db.BigInteger)
    Year_high_price=db.Column(db.BigInteger)
    day=db.Column(db.String(10))

class User_stock_info(db.Model):
    """docstring for [object Object]."""
    __tablename__='user_stock_info'
    id=db.Column(db.BigInteger,primary_key=True)

class Company(db.Model):
    """docstring for [object Object]."""
    id=db.Column(db.Integer,primary_key=True)
    Company_id=db.Column(db.String(65535))
    Logo=db.Column(db.String(65535))
    Name=db.Column(db.String(65535))
    Details=db.Column(db.Text())
    Location=db.Column(db.String(65535))
    Auditors=db.Column(db.String(65535))
    Incorporation_date=db.Column(db.String(65535))
    Listing_Price=db.Column(db.String(65535))
    Shares_Issued=db.Column(db.BigInteger)
    Financial_Year=db.Column(db.String(65535))
    Par_value=db.Column(db.Float)
    Parent_Company=db.Column(db.String(65535))
    Address=db.Column(db.String(65535))
    Website=db.Column(db.String(65535))
    Indices=db.Column(db.String(65535))
    Sector=db.Column(db.String(65535))
