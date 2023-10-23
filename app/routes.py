from app import app
# from app folder import app instance (of Flask class)
from flask import render_template

# Create first route
@app.route('/')
def index():
    name = 'Emili'
    colors = ['red', 'orange', 'yellow', 'green', 'blue']
    return render_template('index.html', first_name=name, last_name="Jansevska", colors=colors)

# Create second route
@app.route('/new')
def new():
    name = 'Emili J'
    colors = ['red', 'orange', 'yellow', 'green', 'blue']
    return f"<h1> Hello {name}, this is a new route!<h1>"