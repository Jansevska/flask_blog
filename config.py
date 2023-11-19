import os

basedir = os.path.abspath(os.path.dirname(__file__))
# C:\\Users\\bstan\\....\\week6\\flask

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # C:\\Users\\bstan\\....\\week6\\flask\\app.db