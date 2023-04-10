import json
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from model.scores import Score

# Creates Blueprint called score_api and establishes url directory
score_api = Blueprint('score_api', __name__,
                   url_prefix='/api/scores')

api = Api(score_api)

class ScoreAPI:        
    class _Create(Resource):
        def post(self):
            # Parses the incoming JSON request data and returns it
            body = request.get_json()
            
            # Checks user inputs, reduce unnecessary data with error checking
            name = body.get('name')
            # If user input of name is less than 2 character, returns 400 error
            if name is None or len(name) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 400
              
            # validate score
            score = body.get('score')
            if score is None or len(score) < 1:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 400

            ''' #1: Key code block, setup USER OBJECT '''
            uo = Score(name=name, 
                      score=score)
            
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            user = uo.create()
            # success returns json of user
            if user:
                return jsonify(user.read())
            # failure returns error
            return {'message': f'Processed {name}, either a format error or User ID {score} is duplicate'}, 400

    class _Read(Resource):
        def get(self):
            users = Score.query.all()    # read/extract all users from database
            json_ready = [user.read() for user in users]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
    

            

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    
