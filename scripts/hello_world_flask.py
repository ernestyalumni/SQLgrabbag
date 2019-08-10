# @file hello_world_flask.py
#
# @ref https://palletsprojects.com/p/flask/
# @ref https://flask.palletsprojects.com/en/1.1.x/quickstart/
# @details
# Make sure not to call your application flask.py because this would conflict
# with Flask itself.
# env FLASK_APP=hello_world_flask.py flask run
#
# An instance of class Flask will be our WSGI (Web Server Gateway Interface)
# application. 
from flask import Flask, escape, request

# Create an instance of Flask class.
# 1st. argument is name of application's module or package. If you're using a
# single module, you should use __name__ because depending on if it's started
# as application or imported as module, name will be different ('__name__')
# versus actual import name). This is needed so that Flask knows where to look
# for templates, static files, etc.
app = Flask(__name__)

# Use route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
def hello():
  """
  @fn hello
  @details Function is given a nmae which is also used to generate URLs for that
  particular function, and returns message we want to display in user's browser.
  """
  name = request.args.get("name", "World")
  return f'Hello, {escape(name)}!'

@app.route('/')
def hello_world():
  return 'Hello, World!' + str(__name__)

