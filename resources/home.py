from flask_restful import Resource
from flask import render_template



class Home(Resource):
    def get(self):
        # return "Welcome to Flask Application"
        return render_template('home.html')
