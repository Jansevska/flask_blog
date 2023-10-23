from flask import Flask

# Create an instance of Flask class
app = Flask(__name__) # name is the current module, here is "hello"

# Create first route
@app.route('/')
def index():
    return '<h1>Hello World!!!<h1>'

# Create second route
@app.route('/new')
def new():
    name = 'Emili Janchevis'
    return f"<h1> Hello {name}, this is a new route!<h1>"