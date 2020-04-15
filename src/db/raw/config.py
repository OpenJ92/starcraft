from flask import Flask
from flask_sqlalchemy import SQLAlchemy

server = Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://jacob:#7572000409Jv@localhost:5432/starcraft'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(server)
