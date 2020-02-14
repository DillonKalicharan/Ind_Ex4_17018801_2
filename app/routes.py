from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import SignUpForm, SearchForm
from app.models import User, City, Forecast


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    cities = City.query.all()
    forecasts = Forecast.query.all()
    print(cities)
    if form.validate_on_submit():
        for city in cities:
            if form.city.data == city.city:
                cityID=city.city_id
                for forecast in forecasts:
                    if forecast.city_id == cityID:
                        flash(f'{forecast.forecast}')
            else:
                flash(f'That city is not in our database ')

        return redirect(url_for('index'))
    return render_template('index.html', cities=cities, forecasts=forecasts, form=form)


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


@app.route('/userinfo')
def user_info():
    users = User.query.all()
    return render_template('userinfo.html', users=users)