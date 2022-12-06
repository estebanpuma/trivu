from app import app, db
from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, WeekData
from app.forms import LoginForm, SignupForm, WeekDataForm
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash('Email incorrecto')
            return redirect(url_for('login'))
        elif not user.check_password(form.password.data):
            flash('Password incorrecto')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, height=form.height.data, birth=form.birth.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Usuario registrado')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)


@app.route('/profile/<email>')
@login_required
def profile(email):
    user = User.query.filter_by(email=email).first_or_404()

    w_data = WeekData.query.filter_by(user_id=user.id).order_by(WeekData.id.desc()).first()


    return render_template('profile.html', user=user, w_data=w_data)

@app.route('/week_data', methods=['GET', 'POST'])
@login_required
def week_data():
   
    form = WeekDataForm()
    if form.validate_on_submit():
        w_data = WeekData(neck=form.neck.data, waist=form.waist.data, weight=form.weight.data, user_id=current_user.id)
        w_data.calc_body_fat()
        db.session.add(w_data)
        db.session.commit()
        return redirect(url_for('index'))
    flash(form.weight.data)
    return render_template('week_data.html', form=form)

    #return render_template('week_data.html', form=form)


@app.route('/diet')
def diet():
    return render_template('diet.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))