#!/usr/bin/python3
""""""

import models
from models.basemodel import BaseModel, Base
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
from os import environ, getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Comments": Comments, "Blog": Blog, 
        "ChosenPath": ChosenPath, "Likes": Likes, 
        "Response": Response, "Requests": Requests, 
        "CommentsLikes": CommentLikes, "Role": Role, 
        "SignUp": SignUp, "Specialization": Specialization, 
        "StudentPoints": StudentPoints
        }

class DBStorage():
    """"""

    __engine = None
    __session = None

    def __init__(self):
        """"""

        mentconnect_user = environ.get('mentconnect_user', 'mentconnect_dev')
        mentconnect_pwd = environ.get('mentconnect_pwd', '')
        mentconnect_host = environ.get('mentconnect_host', 'localhost')
        mentconnect_db = environ.get('mentconnect_db', 'mentconnect_db')
        mentconnect_env = environ.get('mentconnect_env')

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
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return(new_dict)

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

    def close(self):
        """"""
        self.__session.remove()

    def get(self, cls, id):
        """"""
        if cls not in classes.values():
            return None

        all_class = models.storage.all(cls)
        for value in all_class.values():
            if (value.id == id):
                return value
        return None

    def count(self, cls=None):
        """"""
        all_clss = classes.values()
        if not cls:
            count = 0
            for clas in all_clss:
                count +=len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count

