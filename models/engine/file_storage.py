#!/usr/bin/python3
""""""

import json
import models
import os
from models.basemodel import BaseModel
from models.Career_path import CareerPath
from models.Blog import Blog
from models.Chosen_path import ChosenPath
from models.Comments import Comments
from models.Comment_likes import CommentLikes
from models.Likes import Likes
from models.Choose_career import ChooseCareer
from models.Requests import Requests
from models.Response import Response
from models.Role import Role
from models.SignUp import SignUp
from models.Specialization import Specialization
from models.Student_points import StudentPoints

classes = {"CareerPath": CareerPath, "Comments": Comments, "Blog": Blog,
        "ChosenPath": ChosenPath, "ChooseCareer": ChooseCareer, "BaseModel": BaseModel, "Likes": Likes,
        "Response": Response, "Requests": Requests, "CommentsLikes": Comment_Likes, "Role": Role, 
            "SignUp": SignUp, "Specialization": Specialization, "StudentPoints": StudentPoints
            }
class FileStorage:
    """"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """"""
        if cls is not None:
             cls_dict = {}
             for key, value in self.__objects.items():
                    if cls == value.__class__ or cls == value.__class__.__name__:
                    cls_dict[key] = value
             return(cls_dict)
        return self.__objects

    def new(self, obj):
        """"""
        
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """"""

        json_object = {}
        for key, obj in self.__objects.items():
            json_object[key] = obj.to_dict()
        with open(self.__file_path, 'w') as path:
            json.dump(json_object, path)

    def reload(self):
        """"""
        try:
            with open(self.__file_path, 'r') as file:
                jo = json.load(file)
                for key in jo:
                    self.__objects[key] = classes[jo[key]['__class__']](**jo[key])
        except FileNotFoundError:
             pass

    def delete(self, obj=None):
        """"""
        if obj is not None:
            key = obj.__class__.__name__+ '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    """def close(self):
        """"""
        self.reload()

    def get(self, cls, id):
        """"""
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """"""
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())

        else:
            count = len(models.storage.all(cls).values())

        return count"""
