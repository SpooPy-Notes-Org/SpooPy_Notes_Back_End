from flask import Flask, jsonify, request

def create_app(ConfigClass):
    app = Flask(__name__)

    app.config.from_object(ConfigClass)

    with app.app_context():

        @app.route('/ships', methods=['POST'])
        def create_ship():

            return "Hello World"

    return app
