"""
@file database.py
@ref https://flask.palletsprojects.com/en/1.1.x/patterns/sqlalchemy/
https://github.com/graphql-python/graphene-sqlalchemy/blob/master/examples/flask_sqlalchemy/database.py
"""

from sqlalchemy import create_engine
# With scoped_session, SQLAlchemy handles threads.
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
db_session = \
  scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
  # import all modules here that might define models so that
  # they will be registered properly on the metadata. Otherwise
  # you will have to import them first before calling init_db()
  # import yourapplication.models

  from models import Department, Employee, Role

  # Base.metadata.drop_all(bind=engine) # ?

  Base.metadata.create_all(bind=engine)

  # example
  # engineering = Department(name='Engineering')
  # db_session.add(hr)
