
from os.path import dirname, abspath, join
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '0123456789'
CWD = dirname(abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + join(CWD, 'rain.sqlite')
CWD = dirname(abspath(__file__))
db = SQLAlchemy(app)

from app import routes
