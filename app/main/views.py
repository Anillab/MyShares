from flask import current_app as app
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from ..models import User
from .forms import RegistrationForm,LoginForm

@main.route('/')
def dash():
    if current_user.is_authenticated:
        return render_template('dashboard.html')
    return render_template('index.html')

@main.route('/cashout/')
@login_required
def cashout():
    return render_template('cashout.html')

@main.route('/details/<companyid>')
@login_required
def details(companyid):
    return render_template('details.html')

@main.route('/myaccount')
@login_required
def personal():
    return render_template('myaccount.html')


@main.route('/about')
@login_required
def about():
    return render_template('about.html')
