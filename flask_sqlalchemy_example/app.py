#!/usr/bin/env python3
"""
@file app.py
@ref https://github.com/graphql-python/graphene-sqlalchemy/blob/master/examples/flask_sqlalchemy/app.py
"""

from database import db_session, init_db
from flask import Flask

app = Flask(__name__)
app.debug = True

@app.teardown_appcontext
def shutdown_session(exception=None):
  db_session.remove()

@app.route('/')
def hello_world():
  return 'Hello, World!' + str(__name__)

if __name__ == "__main__":
  init_db()
  app.run()