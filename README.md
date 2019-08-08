![spoopy notes in magazine cut-out style](app/assets/spoopy_notes.png)

**Version**: 1.4.0

**Collaborators**: Tammy Do, Skyler Burger, Aliya Summers, Joshua Ho 

**Back End URL**: [https://spoopy-notes.onrender.com](https://spoopy-notes.onrender.com)

**Front End URL**: [https://spoopy-notes.firebaseapp.com/](https://spoopy-notes.firebaseapp.com/)

## Overview
Have you ever wanted to send an anonymous ransom note to someone, but don't have the time to cut out one hundred letters from magazines?   

Save time today! **SpooPy Notes** creates personalized ransom notes for you, simply and quickly. It's easier than breaking into a 1998 Camry!

Use our API to create personalized messages in a ransom note styled output image. Send the image to a recipient or use it as an asset in another project.

## API
- **GET /?query=**: Add a message as the query parameter to generate a ransom note-like image that includes the text you passed in.

- **GET /dadjoke**: Returns a random dad joke from the [icanhazdadjoke API](https://icanhazdadjoke.com/api) in Spoopy Note's ransom note style.

## Architecture
### Packages
- **[flask](https://pypi.org/project/Flask/)**: a Python web application framework
- **[flask_api](https://pypi.org/project/Flask-API/)**: an extension to Flask that adds additional API-specific functionality 
- **[flask_cors](https://pypi.org/project/Flask-Cors/)**: a Flask extension that enables resource sharing between the Flask back and React front end
- **[pillow / PIL](https://pypi.org/project/Pillow/)**: a Python package for image processing
- **[pytest](https://pypi.org/project/pytest/)**: a Python testing framework
- **[requests](https://pypi.org/project/requests/)**: an HTTP library for Python

### Python Standard Library
- **[io](https://docs.python.org/3/library/io.html)**: used for file-less serving of images from the back end
- **[os](https://docs.python.org/3/library/os.html)**: used for pathing to images on the server
- **[random](https://docs.python.org/3/library/random.html)**: used for randomly picking letters
- **[re](https://docs.python.org/3/library/re.html)**: used for validating input from users and external API data

## Change Log

08/05/2019 - **1.1.0**
- Deployed Flask application on Render
- One-line image composition

08/06/2019 - **1.2.0**
- Multi-line image composition
- Back end serving images
- Testing for back end with pytest

08/07/2019 - **1.3.0**
- Refined fonts
- Refactored routes and modules
- Added Dad Joke API integration
- Refined image output

08/08/2019 - **1.4.0**
- Added custom resizing of output image
