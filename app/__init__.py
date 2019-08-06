from app.letters.letters import *
from app.compose_images import *
from flask import Flask, jsonify, request
from flask_cors import CORS

def create_app(ConfigClass):
    app = Flask(__name__)
    CORS(app)

    app.config.from_object(ConfigClass)

    with app.app_context():

        @app.route('/', methods=['GET'])
        def get_spoopy():
            # get query string
            query = request.args.get('query')

            paths = generate_paths(query)
            words = create_word_dictionaries(paths)
            lines = create_lines(words)
            width, height = determine_background(lines)
            image = compose_image(width, height, lines)


            return serve_pil_image(image)

    return app


'''
def text():
   for each letter in text:
        generate img path
   
   return [img path to join]

def list():
    determine background size of image
    paste each image onto background
    return joined image

def determine_canvas(input_images):
    get width of all letters together
    get height of tallest element
    add extra padding of 20 to width
    add extra padding of 20 to height
    use width and height to determine canvas background size
    
    return canvas background size

def compose_image(width, height, images):
    determine a background color for canvas background
    paste letters together with a space of 10px between
    save new image
    
    return new png'''