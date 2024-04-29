from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create an SQLAlchemy object by passing it the application
db = SQLAlchemy(app)
