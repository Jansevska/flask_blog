from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Create an instance of Flask class
app = Flask(__name__)
# Configuring our app with Attributes and Values from the Config class
app.config.from_object(Config)

# Create an instance of SQLAlchemy to represent our database
db = SQLAlchemy(app) # the app as instance of Flask
# Create an instance of migrate to track our database migrations
migrate = Migrate(app, db)


# import routes
from . import routes, models
