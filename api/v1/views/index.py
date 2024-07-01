#!/usr/bin/python3
""""""

from models import storage
from api.v1.views import app_views
from flask import jsonify
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
def status():
    """"""
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """"""
    classes = {"Comments": Comments, "Blog": Blog,
        "ChosenPath": ChosenPath, "Likes": Likes,
        "Response": Response, "Requests": Requests,
        "CommentsLikes": CommentLikes, "Role": Role,
        "SignUp": SignUp, "Specialization": Specialization,
        "StudentPoints": StudentPoints
        }

    names = ["comments", "blogs", "chosenpaths", "likes", 
            "responses","requests", "commentlikes", 
            "roles", "signs", "specializations", 
            "studentspoints"]

    num_objects = {}
    for i in range(len(classes)):
        num_objects[names[i] = storage.count(classes[i])]

    return jsonify(num_objects)
