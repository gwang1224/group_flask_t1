import json
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from model.scores import Score

# Creates Blueprint called score_api and establishes url directory
score_api = Blueprint('score_api', __name__,
                   url_prefix='/api/scores')

api = Api(score_api)

class ScoreAPI:    
    # CRUD function    
    class _Create(Resource):
        def post(self):
            # Parses the incoming JSON request data and returns it
            body = request.get_json()
            
            # Checks user inputs, reduce unnecessary data with error checking
            name = body.get('name')
            # If user input of name is less than 2 character, returns 400 error
            if name is None or len(name) < 2:
                return {'message': f'Name is missing, or is less than 2 characters'}, 400
              
            # validates score
            score = body.get('score')
            # if user does not input score, it gives 400 error message and asks for a score
            if score is None:
                return {'message': f'You did not input a score, please input a score'}, 400
            # since the quiz contains 10 questions, if user inputs a score greater than 10, asks for a valid score
            elif int(score) > 10:
                return {'message': f'Please input a score that is valid: 0 to 10'}, 400


            # setup Score Object, keys name and score
            so = Score(name=name, 
                      score=score)
            
            # create user in scores database
            user = so.create()
            # if creation of user is successful, returns user in json
            if user:
                return jsonify(user.read())
            # failure to create user in database returns error message
            return {'message': f'Unable to store {name}'}, 400

    # CRUD function
    class _Read(Resource):
        def get(self):
            users = Score.query.all()    # reads all users from scores database
            json_ready = [user.read() for user in users]  # formats output in dictionary json format
            return jsonify(json_ready)  # jsonify creates response object
    

    # building RESTapi endpoint with url prefix
    api.add_resource(_Read, '/')
    api.add_resource(_Create, '/create')
    
