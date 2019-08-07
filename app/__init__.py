from app.spoopy import create_note
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_api import status
import requests


def create_app(ConfigClass):
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(ConfigClass)

    with app.app_context():

        @app.route('/', methods=['GET'])
        def get_spoopy():
            if request.args.get('query') != None:
                return create_note(request.args.get('query'))
            else:
                content = {'error': 'invalid'}
                return content, status.HTTP_404_NOT_FOUND

        @app.route('/dadgiggles', methods=['GET'])
        def dad_jokes():
            url = 'https://www.icanhazdadjoke.com'
            headers = {'Accept' : 'application/json'}
            dad_joke = requests.get(url, headers=headers).json()
            print('********DAD JOKE:', dad_joke.get('joke'))

            return create_note(dad_joke.get('joke'))

    return app
