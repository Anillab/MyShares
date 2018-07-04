from flask import current_app as app
from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import RegistrationForm,LoginForm

# with app.app_context():
#     app.config['SECRET_KEY'] = 'kabagemark' 

# Views
# @main.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''

#     title = 'Home'

#     return render_template('index.html', title = title )

@main.route('/register')
def register():
    '''
    View root page function that returns the index page and its data
    '''

    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    title = 'Home'

    return render_template('registration.html', title = title , form = form )

@main.route('/login')
def login():
    '''
    View root page function that returns the index page and its data
    '''

    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    title = 'Home'

    return render_template('login.html', title = title , form = form )     

