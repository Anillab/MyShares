from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , SubmitField, BooleanField, IntegerField, HiddenField
from wtforms.validators import DataRequired , Length , Email , EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])

    email = StringField('Email',validators=[DataRequired(),Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])

    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])

    email = StringField('Email',validators=[DataRequired(),Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Login')

class Buyform(FlaskForm):

    amount = IntegerField('Amount')
    autosell = IntegerField('Autosell: (0 means disabled)')
    company = HiddenField()
    submit = SubmitField("Buy")
