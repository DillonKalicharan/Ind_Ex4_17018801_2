from app import db

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