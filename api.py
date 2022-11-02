from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model_music import *

app_api = Blueprint('api', __name__,
                   url_prefix='/api/music')

# # API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_api)

class TaylorAPI:
    class _Taylor(Resource):
        def get(self):
            return jsonify(initAPI())

    class _UpdateLike(Resource):
        def put(self, album):
            add_like(album)
            return jsonify(fav_albums)


    api.add_resource(_Taylor, '/taylor')
    api.add_resource(_UpdateLike, '/likes')