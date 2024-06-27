#!/usr/bin/python3
""""""

import models
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
from os import environ, getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import scoped_session, sessionmaker

classes = {"CareerPath": CareerPath, "Comments": Comments, "Blog": Blog,
        "ChosenPath": ChosenPath, "ChooseCareer": ChooseCareer, "BaseModel": BaseModel, "Likes": Likes,
        "Response": Response, "Requests": Requests, "CommentsLikes": Comment_Likes, "Role": Role, 
            "SignUp": SignUp, "Specialization": Specialization, "StudentPoints": StudentPoints
            }

class DBStorage:
    """"""

    __engine = None
    __session = None

    def __init__(self):
        """"""

        mentconnect_user = environ.get('mentconnect_user', 'mentconnect_dev')
        mentconnect_pwd = environ.get('mentconnect_pwd', '')
        mentconnect_host = environ.get('mentconnect_host', 'localhost')
        mentconnect_db = environ.get('mentconnect_db', 'mentconnect_db')
        mentconnect_env = environ.get('mentconnect_env', 'mentconnect_env')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                    format(mentconnect_user,
                                        mentconnect_pwd,
                                        mentconnect_host,
                                        mentconnect_db))

        if mentconnect_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """"""

        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[cls] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
                return new_dict
        return self.__objects

    def new(self, obj):
        """"""

        self.__session.add(obj)

    def save(self):
        """"""

        self.__session.commit()

    def delete(self, obj=None):
        """"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """"""

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

