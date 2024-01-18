# GrammarChecker
This repository contains an exam exercise from Paulius Smirnovas from DIEf-21 group

My Cool Flask App
About
This is a web application that checks the grammar and spelling of a given English text. It uses the Flask framework to serve the web pages, and the language_tool_python library to perform the grammar and spelling checks.

Components
Flask Framework
Flask is a micro web framework written in Python. It was chosen for this application due to its simplicity and flexibility. Flask allows for fast setup, and easy integration with libraries like language_tool_python.

language_tool_python
language_tool_python is a Python wrapper for LanguageTool. LanguageTool is an open-source spelling and grammar checker for more than 20 languages. In this application, it is used to check the grammar and spelling of the user's input text and suggest corrections.

How the Program Works
app.py
This file contains the main Flask application. It defines the routes for the application and the logic for processing user input.

When the user submits the text, the grammar_check() function is called to check the text for grammar and spelling errors. The result is a list of errors, each with the context, the error message, and the suggested corrections.

Then, the fix_sentence() function is called to automatically correct the errors in the text. The result is the corrected text.

The original text, the list of errors, and the corrected text are stored in session variables so they can be displayed to the user.

index.html
This file is the template for the main page of the web application. It contains a form for the user to enter their text, and areas to display the original text, the grammar check results, and the corrected text.

The page also includes a button to clear the output and a button to toggle a rainbow effect on the output.

Requirements
Python 3.6 or higher
Flask
language_tool_python
Installation
Clone this repository
Install the requirements: pip install -r requirements.txt
Run the application: python app.py
