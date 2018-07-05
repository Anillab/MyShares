from flask import current_app as app
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user,login_user,logout_user
from . import auth
from ..models import User,saveobject
from .forms import RegistrationForm,LoginForm

@auth.route('/register',methods=["GET","POST"])
def register():
    '''
    View root page function that returns the index page and its data
    '''

    form = RegistrationForm()
    if form.validate_on_submit():
        user=form.username.data
        passw=form.password.data
        email=form.email.data
        if not User.query.filter(User.username==user).first():
            tempuser=User(username=user,password=passw,email=email)
            saveobject(tempuser)
            login_user(tempuser)
            return redirect(url_for('main.dash'))
    title = 'Home'
    return render_template('registration.html', title = title , form = form )

@auth.route('/signout',methods=["GET","POST"])
def logout():
    if current_user.is_authenticated:
        logout_user()
    title = 'Home'
    return redirect(url_for('auth.login'))

@auth.route('/login',methods=["GET","POST"])
def login():
    '''
    View root page function that returns the index page and its data
    '''

    form = LoginForm()
    if form.validate_on_submit():
        user=form.username.data
        passw=form.password.data
        if User.query.filter(User.username==user).first():
            tempuser=User.query.filter(User.username==user).first()
            if tempuser.verify_password(passw):
                print('Umepenya')
                login_user(tempuser,form.remember.data)
                return redirect(url_for('main.dash'))
    title = 'Home'
    return render_template('login.html', title = title , form = form )
