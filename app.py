"""
This module contains the Flask application for TimeEntryDE.
"""
import logging
import os
from logging.handlers import FileHandler
from flask import Flask, render_template, redirect, url_for, request, make_response
from flask_login import LoginManager, login_user
from models import User
from forms import RegistrationForm
from database import db

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    """
    Load user by user_id
    """
    app.logger.debug('load_user function')
    return User.query.get(int(user_id))

@app.route('/')
def index():
    """
    Index route
    """
    app.logger.debug('index function')
    response = make_response(render_template('index.html'))
    response.headers['Content-Type'] = 'text/html'
    return response

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login route
    """
    app.logger.debug('login function')
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
    # Register route
def register():
    app.logger.debug('register function')
    response = make_response(render_template('register.html'))
    response.headers['Content-Type'] = 'text/html'
    return response




if __name__ == '__main__':
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    LOGFILE = 'app.log'
    LOG_HANDLER = FileHandler(LOGFILE)
    LOG_HANDLER.setLevel(logging.DEBUG)
    app.logger.addHandler(LOG_HANDLER)
    app.logger.debug('app.py main function')
    app.run()