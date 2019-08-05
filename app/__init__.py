from flask import Flask, jsonify, request

def create_app(ConfigClass):
    app = Flask(__name__)

    app.config.from_object(ConfigClass)

    with app.app_context():

        @app.route('/', methods=['GET'])
        def get_spoopy():

            return "Hello World"

    return app
