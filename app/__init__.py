from flask import Flask

# Create an instance of Flask class
app = Flask(__name__) # name is the current module, here is "hello"

# import routes
from . import routes
