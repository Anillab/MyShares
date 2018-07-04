from flask import render_template,request,redirect,url_for,abort
from . import main
from ..requests import get_todays,get_companies

# Views
@main.route('/')
def index():
    title = 'Home'
    todays = get_todays()
    companies = get_companies()
    return render_template('index.html', title = title ,todays=todays, companies=companies)
