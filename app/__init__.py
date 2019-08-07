from app.spoopy import create_note
from flask import Flask, jsonify, request
from flask_cors import CORS

def create_app(ConfigClass):
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(ConfigClass)

    with app.app_context():

        @app.route('/', methods=['GET'])
        def get_spoopy():
            return create_note(request.args.get('query'))

    return app
