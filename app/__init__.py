# -*- coding: utf-8 -*-

from flask import Flask
from flask_mysqldb import MySQL
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask("balance")


#app.config['SECRET_KEY'] = 'random'
# app.debug = True
# toolbar = DebugToolbarExtension(app)

from app import config

mysql = MySQL(app)

from app.controllers import *