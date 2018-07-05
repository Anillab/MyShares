from flask import current_app as app
from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from ..models import User,Company,Stock_Info,STOCKSHistory
from .forms import RegistrationForm,LoginForm
from scipy.signal import savgol_filter
import pygal
from pygal.style import DarkSolarizedStyle
import calendar

@main.route('/')
def dash():
    if current_user.is_authenticated:
        companies = Company.query.all()
        values = Stock_Info.query.all()
        return render_template('dashboard.html',companies=companies, values=values)
    return render_template('index.html')

@main.route('/orders/')
@login_required
def cashout():
    return render_template('Orders.html')

@main.route('/details/<companyid>')
@login_required
def details(companyid):
    data=STOCKSHistory.get_stocks(companyid)
    if not data:
        return render_template('details.html',chartdata=None)
    bar_chart = pygal.Line(truncate_legend=-1,width=600, height=500,style=DarkSolarizedStyle)
    x_labels=[i['DATE'] for i in data]
    highs=[i['high'] for i in data]
    closes=[i['close'] for i in data]
    low=[i['low'] for i in data]
    closessmooth=savgol_filter(closes,25,4)
    highsmooth=savgol_filter(highs,25,4)
    lowsmooth=savgol_filter(low,25,4)
    labelred = lambda x: '.' if not x.endswith('-25') else calendar.month_name[int(x[5:7])]
    bar_chart.x_labels = map(labelred,x_labels)
    bar_chart.add('Closing',closessmooth)
    bar_chart.add('Lowest ',lowsmooth)
    bar_chart.add('Highest',highsmooth)
    charthtml=bar_chart.render().decode()
    return render_template('details.html',chartdata=charthtml)

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
