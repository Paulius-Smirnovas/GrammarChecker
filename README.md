# GrammarChecker
This repository contains an exam exercise from Paulius Smirnovas from DIEf-21 group

My Cool Flask App

About

This is a web application that checks the grammar and spelling of a given English text. It uses the Flask framework to serve the web pages, and the language_tool_python library to perform the grammar and spelling checks.

Components

Flask Web Framework

Flask is a micro web framework written in Python. It's lightweight, easy to use, and it's perfect for small scale projects like this one. It is used in this project to serve the web pages, handle requests and responses, and manage sessions. Flask allows for fast setup, and easy integration with libraries like language_tool_python.

language_tool_python

language_tool_python is a Python wrapper for LanguageTool. LanguageTool is an open-source spelling and grammar checker for more than 20 languages. In this application, it is used to check the grammar and spelling of the user's input text and suggest corrections.

How the Program Works

app.py

This file contains the main Flask application. It defines the routes for the application and the logic for processing user input.

When the user submits the text, the grammar_check() function is called to check the text for grammar and spelling errors. The result is a list of errors, each with the context, the error message, and the suggested corrections.

Then, the fix_sentence() function is called to automatically correct the errors in the text. The result is the corrected text.

The original text, the list of errors, and the corrected text are stored in session variables so they can be displayed to the user.

Main functions and important notes : 

grammar_check(text): This function receives a string of text as input, checks it for grammar errors using the LanguageTool library, and returns a list of Match objects representing the found errors.

fix_sentence(text): This function receives a string of text as input, corrects the grammar errors using the LanguageTool library, and returns the corrected text as a string.

app = Flask(__name__): Here we're creating an instance of the Flask class for our web application.

app.config['SECRET_KEY'] = 'your_secret_key': This is used to keep the client-side sessions secure.

@app.route('/', methods=['GET', 'POST']): This decorator tells Flask what URL should trigger the index() function. The methods parameter is a list that specifies the HTTP methods that should be accepted by this function.

session: It's a built-in object in Flask that allows you to store information specific to a user from one request to the next.

request.form: It's a type of MultiDict object which is used to handle form data sent as POST or PUT request.


index.html

This file is the template for the main page of the web application. It contains a form for the user to enter their text, and areas to display the original text, the grammar check results, and the corrected text.

The page also includes a button to clear the output and a button to toggle a rainbow effect on the output.

form method="POST": This is the form that users will enter their text into. When the form is submitted, it triggers a POST request to the server.

input type="text": This is the text input field where users will enter their text.

input type="submit": These are the buttons for submitting the form and clearing the output.

button type="button": This is the button for toggling the rainbow effect.

div class="grammar-results": This div contains the results of the grammar check. It is populated by iterating over each match in the matches list and creating a table row for each one.

div class="fixed-sentences": This div contains the corrected text.


Results

When a user inputs text and submits the form, the text is sent to the server where it is checked for grammar and spelling errors. The server then returns the original text, a list of the errors, and the corrected text. This information is displayed to the user on the webpage.

The user can then choose to clear the output, toggle a rainbow effect on the output, or enter new text to be checked.



Requirements

Python 3.6 or higher

Flask

language_tool_python

Installation

Clone this repository

Install the requirements: pip install -r requirements.txt

Run the application: python app.py




The main requirements should be :

Flask==2.0.1

language_tool_python==2.5.3

And their dependencies

My whole environment at the time is lsited in the requirements.txt. (Note, most of these are not needed for this program to work. But it would be best to match these by writing these into a requirements.txt file and intalling them in order to avoid conflicts).

