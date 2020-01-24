from app import app
from flask import render_template



@app.route('/')
def index():
    user = {'username' : 'Vasya'}
    return render_template('home_page/index.html', title='Уборка квартир', user=user)


@app.route('/general_clean')
def general_clean():
    return render_template('general_clean/general_clean.html', title='Генеральная уборка')


@app.route('/repair_clean')
def repair_clean():
    return render_template('repair_clean/repair_clean.html')


@app.route('/window_clean')
def window_clean():
    return render_template('window_clean/window_clean.html')


@app.route('/support_clean')
def support_clean():
    return render_template('support_clean/support_clean.html')


@app.route('/office_clean')
def office_clean():
    return render_template('office_clean/office_clean.html')