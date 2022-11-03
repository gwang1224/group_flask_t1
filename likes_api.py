from flask import Blueprint, jsonify
from flask_restful import Api, Resource
from likes_data import *

likes_api = Blueprint('l_api', __name__, 
                            url_prefix='/api/likes')

l_api = Api(likes_api)

class LikesAPI:
    class _Expose(Resource):
        def get(self):
            return jsonify(getData())

    class _GetLikes(Resource):
        def get(self, song):
            return jsonify(getLikes(song))

    class _IncrementLikes(Resource):
        def get(self, song):
            return jsonify(incrementLikes(song))

    l_api.add_resource(_Expose, "/")
    l_api.add_resource(_GetLikes, "/<string:song>/likes")
    l_api.add_resource(_IncrementLikes, "/<string:song>/increment_likes")