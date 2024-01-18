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



The main requirements should be :
Flask==2.0.1
language_tool_python==2.5.3


My whole environment at the time was (Note, most of these are not needed for this program to work. But it would be best to match these by writing these into a requirements.txt file and intalling them):
absl-py==2.1.0
annotated-types==0.6.0
anyio==3.7.1
astunparse==1.6.3
blinker==1.6.3
cachetools==5.3.2
certifi==2023.11.17
charset-normalizer==3.3.2
click==8.1.7
colorama==0.4.6
dm-tree==0.1.8
fastapi==0.104.1
Flask==2.2.5
Flask-Login==0.6.2
Flask-SQLAlchemy==3.1.1
flatbuffers==23.5.26
gast==0.5.4
google-auth==2.26.2
google-auth-oauthlib==1.2.0
google-pasta==0.2.0
greenlet==3.0.0
grpcio==1.60.0
h11==0.14.0
h5py==3.10.0
idna==3.4
itsdangerous==2.1.2
Jinja2==3.1.2
joblib==1.3.2
keras==2.15.0
language-tool-python==2.7.1
libclang==16.0.6
Markdown==3.5.2
markdown-it-py==3.0.0
MarkupSafe==2.1.3
mdurl==0.1.2
ml-dtypes==0.2.0
namex==0.0.7
nltk==3.8.1
numpy==1.26.0
oauthlib==3.2.2
opt-einsum==3.3.0
packaging==23.2
paho-mqtt==1.6.1
pandas==2.1.1
protobuf==4.23.4
pyasn1==0.5.1
pyasn1-modules==0.3.0
pydantic==2.5.2
pydantic_core==2.14.5
Pygments==2.17.2
python-dateutil==2.8.2
pytz==2023.3.post1
pywin32==306
regex==2023.12.25
requests==2.31.0
requests-oauthlib==1.3.1
rich==13.7.0
rsa==4.9
scikit-learn==1.3.1
scipy==1.11.3
six==1.16.0
sklearn==0.0.post10
sniffio==1.3.0
SQLAlchemy==2.0.22
starlette==0.27.0
tensorboard==2.15.1
tensorboard-data-server==0.7.2
tensorflow==2.15.0
tensorflow-estimator==2.15.0
tensorflow-intel==2.15.0
tensorflow-io-gcs-filesystem==0.31.0
termcolor==2.4.0
threadpoolctl==3.2.0
tornado==6.3.3
tqdm==4.66.1
typing_extensions==4.8.0
tzdata==2023.3
urllib3==2.1.0
uvicorn==0.24.0.post1
Werkzeug==2.2.2
wrapt==1.14.1
