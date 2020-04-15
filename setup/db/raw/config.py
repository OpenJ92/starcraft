import dash
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://jacob:#7572000409Jv@localhost:5432/starcraft'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(server)
