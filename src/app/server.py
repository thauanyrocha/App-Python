from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://thauany@pythonbd:Bancodedados123#@pythonbd.mysql.database.azure.com/pythonbd'

db = SQLAlchemy(app)
