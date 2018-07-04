from robobrowser import RoboBrowser

r= RoboBrowser(parser="lxml")
r.open('https://abacus.co.ke/auth/login')

login_form=r.get_form()
login_form['username']='xvier'
login_form['password']='yozjiurfUsMann1'
login_form['remember']='on'
login_form.serialize()

r.submit_form(login_form)]
base_url='https://abacus.co.ke/live/company/{}/summary'
def get_chart(company):
    r.open(base_url.format(company))
    data=r.find_all('script')[8].text[19:-2]
    return data
