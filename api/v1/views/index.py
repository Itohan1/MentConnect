#!/usr/bin/python3
""""""

from models import storage
from api.v1.views import app_views
from flask import jsonify, Flask, Response
import json
from models.Blog import Blog
from models.Chosen_path import ChosenPath
from models.Comments import Comments
from models.Comment_likes import CommentLikes
from models.Likes import Likes
from models.Requests import Requests
from models.Response import Response
from models.Role import Role
from models.sign import SignUp
from models.Specialization import Specialization
from models.Student_points import StudentPoints

@app_views.route('/status', methods=['Get'], strict_slashes=False)
def show():
    """"""
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def count():
    """"""

    response = {"comments": storage.count(Comments), 
            "blogs": storage.count(Blog), 
            "chosenpaths": storage.count(ChosenPath), 
            "likes": storage.count(Likes), 
            "responses": storage.count(Response), 
            "requests": storage.count(Requests), 
            "commentlikes": storage.count(CommentLikes), 
            "roles": storage.count(Role), 
            "signs": storage.count(SignUp), 
            "specializations": storage.count(Specialization), 
            "studentspoints": storage.count(StudentPoints)
            }

    postresponse = jsonify(response)
    return postresponse
