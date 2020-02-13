from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import SignUpForm
from app.models import User, City, Forecast


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        flash(f'It worked :D')
        user = User(username=form.username.data, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('signup.html', form=form)
