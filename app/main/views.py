from flask import current_app as app
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from ..models import User,STOCKSHistory
from .forms import RegistrationForm,LoginForm
import pygal
from pygal.style import DarkSolarizedStyle

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/orders/')
@login_required
def cashout():
    return render_template('Orders.html')

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

@main.route('/dashboard')
@login_required
def dash():
    return render_template('dashboard.html')

@main.route('/dashboard')
@login_required
def get_chart_data():
    data=STOCKSHistory.get_stocks('BAMB')
    bar_chart = pygal.Line(width=1200, height=600, explicit_size=True, title='Bamburi Stocks',x_label_rotation=30)
    bar_chart.x_labels = [i['DATE'] for i in data]
    bar_chart.add('Closing ',[i['close'] for i in data])
    # bar_chart.add('Low ',[i['low'] for i in data])
    # bar_chart.add('High ',[i['high'] for i in data])
    return render_template('dashboard.html',chartdata=bar_chart.render())
