from flask import current_app as app
from flask import render_template,request,redirect,url_for,abort,flash
from flask_login import login_required,current_user
from . import main
from ..models import User,Company,Stock_Info,STOCKSHistory
from .forms import RegistrationForm,LoginForm,Buyform
from scipy.signal import savgol_filter
from ..requests import *
import pygal
from pygal.style import DarkSolarizedStyle
import calendar

@main.route('/')
def index():
    get_companies()
    get_todays()
    return render_template('index.html')

@main.route('/dashboard')
@login_required
def dash():
    companies = Company.query.all()
    values = Stock_Info.query.all()
    return render_template('dashboard.html',companies=companies, values=values)

@main.route('/order/')
@login_required
def cashout():
    # form=Buyform()
    # if form.validate_on_submit():
    #     companyid=form.companyid.data
    #     amount=form.amount.data
    #     output=current_user.buystocks(companyid,amount)
    #     if output:
    #         flash(output,'error')
    #         return render_template('Orders.html')
    #     return redirect(url_for('main.dash'))
    return render_template('Orders.html')

@main.route('/details/<companyid>',methods=["GET","POST"])
@login_required
def details(companyid):
    company = Company.query.filter(Company.Company_id==companyid).first()
    form=Buyform(company=company.id)
    if form.validate_on_submit():
        amountform=form.amount.data
        companyidform=form.company.data
        output=current_user.buystocks(companyidform,amountform)
        if output:
            flash(output,'error')
        else:
            return redirect(url_for('main.dash'))
    data=STOCKSHistory.get_stocks(companyid)
    company = Company.query.filter(Company.Company_id==companyid).first()
    if not data:
        return render_template('details.html',chartdata=None,company=company)
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
    return render_template('details.html',chartdata=charthtml,company=company,form=form)

@main.route('/sell/<int:id>')
@login_required
def seller(id):
    current_user.sellstocks(id)
    return render_template('myaccount.html')

@main.route('/myaccount')
@login_required
def personal():
    return render_template('myaccount.html')


@main.route('/about')
@login_required
def about():
    return render_template('about.html')


# @main.route('/dashboard')
# @login_required
# def get_chart_data():
#     data=STOCKSHistory.get_stocks('BAMB')
#     bar_chart = pygal.Line(width=1200, height=600, explicit_size=True, title='Bamburi Stocks',x_label_rotation=30)
#     bar_chart.x_labels = [i['DATE'] for i in data]
#     bar_chart.add('Closing ',[i['close'] for i in data])
#     # bar_chart.add('Low ',[i['low'] for i in data])
#     # bar_chart.add('High ',[i['high'] for i in data])
#     return render_template('dashboard.html',chartdata=bar_chart.render())
