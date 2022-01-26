from flask import Blueprint, render_template, request

views = Blueprint(__name__, 'views')


@views.route('/')
def home():
    return render_template('index.html', name='Tri')


@views.route('/homepage')
def homepage():
    return render_template('homepage.html')

@views.route('/calender')
def calender():
    return render_template('calender.html')
