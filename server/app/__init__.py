from flask import Flask
from flask_sqlalchemy import SQLAlchemy

hub = Flask(__name__)
# Configure the SQLAlchemy part of the app instance, details temporary for now
hub.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/mydatabase'
hub.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Iterating a SQLAlchemy object by passing it the application
db = SQLAlchemy(hub)