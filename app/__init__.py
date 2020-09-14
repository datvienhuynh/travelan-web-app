import os
# import urllib.parse
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# db_string = os.environ['dbstring']
# params = urllib.parse.quote_plus(db_string)

# # initialization
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'supersecret'
# app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Get the directory path of file
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

# Create a path to the sqlite file from the directory path above
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Wrap a Flask-Alchemy instance around the Flask Application
db = SQLAlchemy(app)

from app import routes