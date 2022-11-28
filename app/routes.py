from app import app
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/week_data')
def week_data():
    return render_template('week_data.html')