# Import the necessary modules from the Flask and language_tool_python libraries
from flask import Flask, request, render_template, session, redirect, url_for
import language_tool_python

# This function takes a string of text as input, checks it for grammar errors using the LanguageTool library,
# and returns a list of Match objects representing the found errors.
def grammar_check(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    return matches

# This function takes a string of text as input, corrects the grammar errors using the LanguageTool library,
# and returns the corrected text as a string.
def fix_sentence(text):
    tool = language_tool_python.LanguageTool('en-US')
    fixed_text = tool.correct(text)
    return fixed_text

# Create a Flask application instance
app = Flask(__name__)
# Set a secret key for the application, which is necessary for Flask's session functionality.
# You should replace 'your_secret_key' with your own secret key.
app.config['SECRET_KEY'] = 'your_secret_key'

# Define the route for the application's root URL.
# The route accepts both GET and POST requests: GET to display the form and POST to process the submitted text.
@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize the session variables if they are not already set.
    if 'text' not in session:
        session['text'] = ''
    if 'matches' not in session:
        session['matches'] = []
    if 'fixed_text' not in session:
        session['fixed_text'] = ''

    # If the request method is POST, process the submitted text.
    if request.method == 'POST':
        # If the 'text' field is filled, check the grammar of the text and store the result in the session.
        if 'text' in request.form and request.form.get('text').strip():
            text = request.form.get('text')
            matches = grammar_check(text)
            session['text'] = text
            session['matches'] = [{'error': m.context, 'msg': m.message, 'replacements': m.replacements} for m in matches]
            # Correct the text and store the result in the session.
            session['fixed_text'] = fix_sentence(text)
        # If the 'clear' button is clicked, clear the session variables.
        if 'clear' in request.form:
            session['text'] = ''
            session['matches'] = []
            session['fixed_text'] = ''

    # Render the index.html template and pass the session variables to it.
    return render_template('index.html', text=session['text'], matches=session['matches'], fixed_text=session['fixed_text'])

#Run the application. If the script is run directly (not imported), turn on debug mode.
if __name__ == '__main__':
    app.run(debug=True)
