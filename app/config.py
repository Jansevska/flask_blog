import os

basedir = os.path.abspath(os.path.dirname(__file__))
# C:\\Users\\bstan\\....\\week6\\flask

class Config:
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    # C:\\Users\\bstan\\....\\week6\\flask\\app.db