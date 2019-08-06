# SpooPy Notes
**Author**: Tammy Do, Skyler Burger, Aliya Summers, Joshua Ho 
**Version**: 1.0.0


## Overview
Have you ever wanted to send an anonymous, threatening ransom note to someone, but don't have time between kidnappings and bank heists to cut out one hundred letters from magazines?   

Save time today - "SpooPy Notes" creates personalized ransom notes for you, simply and quickly. It's easier than breaking into a 1998 Camry!

Use one of our pre-designed (and tested) templates to coerce your targets into adding bitcoins to your off-shore bank account. Or, write your own message for that special, personalized touch, you casanova.

## Getting Started
Head to our app and enter your ransom message. The app will turn your text into an image of a creepy ransom note. 

## Architecture
- [Pillow](https://python-pillow.org/): for image processing
- [React](https://reactjs.org/): web framework for frontend

## API
<!-- Provide detailed instructions for your applications usage. This should include any methods or endpoints available to the user/client/developer. Each section should be formatted to provide clear syntax for usage, example calls including input data requirements and options, and example responses or return values. -->

## Change Log

08-05-2019  
- Set up basic Flask application onto render - https://spoopy-notes.onrender.com 
- Added basic router
- Created two repositories - frontend and backend
- Updated ownership and collaboration settings for organization and repositories
- Uploaded initial file structure for both repositories

## User Stories
- As someone who wants to scare their friends, I want to be able to make spooky notes without involving craft supplies.
- As a developer, I want an easy to use back-end that is well-documented and commented.
- As a developer, I want a home route so that my app will have a front page for the user to request a ransom note and receive it in ransom form.
- As a developer, I want a random letter picker that will return the letters the user requested.
- As a developer, I want tests that confirm my app works as expected. Including status codes for routes, image byte comparison, etc.
- As a developer, I want an appropriate file structure so that other developers can easily understand the content. 
- As a user, I want an easy to use interface that allows me to quickly create my own spooky note.
- As a receiver of a note, I want a visually interesting note that shows each letter in a variety of fonts and colors. 
