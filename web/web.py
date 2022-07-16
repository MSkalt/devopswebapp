from flask import Flask,  request, jsonify, make_response,render_template
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import os
import signal




# create an instance of flask
app = Flask(__name__, template_folder='templates')
@app.route('/')

def get_all_Employees():

 return render_template('web.html')


app.route("/")
def get_all_Employees(id):
    user_name = get_all_Employees(id)
    return "<H1 id='user'>" + user_name + "</H1>"