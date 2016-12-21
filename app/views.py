from flask import render_template

from app import app
from app.forms import LoginForm
from app import db
from flask import request
from flask import session

@app.route('/login', methods=['GET'])
def login():
    form = LoginForm()
    return render_template('login.html',
                           title='Sign In',
                           form=form)

@app.route('/login', methods=['POST'])
def authentication():

    return render_template('base.html')