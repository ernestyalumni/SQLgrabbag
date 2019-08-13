# @file __init__.py
# @ref https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/

from pathlib import (Path, PurePath)

# @ref https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/
# A Flask application is an instance of the Flask class. Everything about the
# application, such as configuration and URLs, will be registered with this
# class.
# While it's simple and useful to create a global Flask instance directly at
# the top of your code, it can cause tricky issues as project grows.
# Instead of creating Flask instance globally, create it inside a function.
# This function is known as the application factory. Any configuration,
# registration, and other setup the application needs will happen inside the
# function, then the application will be returned.
from flask import Flask

def create_app(test_config=None):
  # create and configure the app
  #
  # app = Flask(__name__, instance_relative_config=True) creates the Flask
  # instance.
  # * __name__ is the name of current Python module. App needs to know where
  # it's located to set up some paths, and __name__ is a convenient way to tell
  # it that.
  # * instance_relative_config=True tells the app that configuration files are
  # relative to the instance folder. The instance folder is located outside the
  # flaskr package and can hold local data that shouldn't be committed to
  # version control, such as configuration secrets and the database file.
  app = Flask(__name__, instance_relative_config=True)

  # app.config.from_mapping() sets some default configuration that the app will
  # use.
  # * SECRET_KEY used by Flask and extensions to keep data safe. It's set to
  # 'dev' to provide a convenient value during development, but should be
  # overridden with a random value when deploying.
  # * DATABASE is the path where SQLite database file will be saved. It's under
  # app.isntance_path, which is the path that Flask has chosen for the instance
  # folder. You'll learn more about the database in the next section.
  app.config.from_mapping(
    # a default secret that should be overridden by instance config
    SECRET_KEY='dev',
    # store the database in the instance folder
    #DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    DATABASE=str(PurePath.joinpath(Path(app.instance_path), 'flaskr.sqlite'))
  )

  if test_config is None:
    # load the instance config, if it exists, when not testing
    #
    # app.config.from_pyfile() overrides the default configuration with values
    # taken from the config.py file in the instance folder if it exists. For
    # example, when deploying, this can be used to set a real SECRET_KEY
    # test_config can also be passed to the factory, and will be used instead
    # of the instance configuration. This is so tests you'll write later in the
    # tutorial can be configured independently of any development values you
    # have configured.
    app.config.from_pyfile('config.py', silent=True)
  else:
    # load the test config if passed in
    app.config.from_mapping(test_config)

  # ensure the instance folder exists
  try:
    # Flask doesn't create the instance folder automatically, but it needs to
    # be created because your project will create the SQLite database file
    # there.
    # cf. https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir
    # If parents is true, any missing parents of this path are created as
    # needed; they're created with the default permissions without taking mode
    # into account (mimicking the POSIX mkdir -p command).
    # exist_ok false (default), FileExistsError raised if target directory
    # already exists.
    Path(app.instance_path).mkdir(parents=True)
  except (OSError, FileExistsError):
    pass

  # @app.route() creates a simple route so you can see the application working
  # before getting into the rest of the tutorial. It creates a connection
  # between the URL /hello and a function that returns a response, the string
  # 'Hello, World!' in this case
  @app.route("/hello")
  def hello():
    return "Hello, World!"

  # register the database commands
  #from flaskr import db

  #db.init_app(app)

  # apply the blueprints to the app
  #from flaskr import auth, blog

  #app.register_blueprint(auth.bp)
  #app.register_blueprint(blog.bp)

  # make url_for('index') == url_for('blog.index')
  # in another app, you might define a separate main index here with
  # app.route, while giving the blog blueprint a url_prefix, but for
  # the tu

  return app