from app import app
                                    # from app folder import app instance (of Flask class)
from flask import render_template, redirect, url_for
                                    # Import SignUpForm class from forms
from app.forms import SignUpForm

# Create first route
@app.route('/')
def index():
    return render_template('index.html')

# Create second route
@app.route('/signup', methods=['GET','POST'])
def signup():
    # create instance of the signupform
    form = SignUpForm()
    if form.validate_on_submit():
        # Get the data from each of the fidls
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(first_name, last_name, username, email, password)
        
        # Redirect back to the home page
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)