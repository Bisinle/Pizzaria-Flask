from flask import Flask
from flask_restful import Resource, Api

# create both app and api instances
app = Flask(__name__)
api = Api(app)


from  api import routes