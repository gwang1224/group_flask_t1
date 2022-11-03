from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from test import *

app_api = Blueprint('api', __name__,
                   url_prefix='/api/music')

# # API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_api)

class TaylorAPI:
    class _Taylor(Resource):
        def get(self):
            return jsonify(initAPI())


    # Help :(
    class _UpdateLike(Resource):
        def put(self):
            add_like(album)
            return jsonify(getLikes())


    api.add_resource(_Taylor, '/taylor') # Why is this not showing up on web server :(
    api.add_resource(_UpdateLike, '/likes') # Help :(