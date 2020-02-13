from flask import Flask, render_template, flash, redirect, url_for
from os.path import dirname, abspath, join
from forms import SignUpForm
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '0123456789'
CWD = dirname(abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + join(CWD, 'rain.sqlite')
CWD = dirname(abspath(__file__))
db = SQLAlchemy(app)
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    forecasts = db.relationship('Forecast', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username,}','{self.email,}','{self.user_id,}')"


class City(db.Model):
    city_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(250), nullable=False)
    forecasts = db.relationship('Forecast', backref='city', lazy=True)


class Forecast(db.Model):
    forecast_id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.city_id'),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    forecast_datetime = db.Column(db.String(250), nullable=False)
    forecast = db.Column(db.VARCHAR(250), nullable=False)
    comment = db.Column(db.VARCHAR(250), nullable=False)

    def __repr__(self):
        return f"Post('{self.city_id}', '{self.forecast}')"


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        flash(f'It worked :D')
        return redirect(url_for('index'))

    return render_template('signup.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
