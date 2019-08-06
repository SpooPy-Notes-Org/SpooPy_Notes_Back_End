from flask import Flask, jsonify, request

def create_app(ConfigClass):
    app = Flask(__name__)

    app.config.from_object(ConfigClass)

    with app.app_context():

        @app.route('/', methods=['GET'])
        def get_spoopy():

            return "Hello World"

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