#!/usr/bin/python3
""""""

from models.Blog import Blog
from models.Chosen_path import ChosenPath
from models.Comments import Comments
from models.Comment_likes import CommentLikes
from models.Likes import Likes
from models.Requests import Requests
from models.Response import Response
from models.Role import Role
from models.Specialization import Specialization
from models.Student_points import StudentPoints
from os import environ
from models.sign import SignUp
from models import storage
from flask import Flask, render_template
app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

@app.route('/', strict_slashes=False)
def home():
    return render_template('SignUp.html')

@app.route('/choosepath', strict_slashes=False)
def choosepath():
    return render_template('choosepath.html')

@app.route('/Role', strict_slashes=False)
def role():
    return render_template('Role.html')

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)

