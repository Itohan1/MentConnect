#!/usr/bin/python3
""""""

import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Table, Integer, DateTime
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
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel, Base


class SignUp(BaseModel, Base):
    """"""
    if models.storage_t == 'db':
        __tablename__ = "sign"
        email = Column(String(200), nullable=False)
        firstname = Column(String(200), nullable=False)
        age = Column(String(200), nullable=False)
        surname = Column(String(200), nullable=False)
        password = Column(String(200), nullable=False)
        likes = relationship("Likes", backref="sign")
        blog = relationship("Blog", backref="sign")
        comments = relationship("Comments", backref="sign")
        roles = relationship("Role", backref="sign")
        specializations = relationship("Specialization", backref="sign")
        request = relationship("Requests", backref="sign")
        response = relationship("Response", backref="sign")
        points = relationship("StudentPoints", backref="sign")
        chosenpaths = relationship("ChosenPath", backref="sign")
    else:
        email = ''
        firstname = ''
        age = ''
        surname = ''
        password = ''

    def __init__(self, *args, **kwargs):
        """"""

        super().__init__(*args, **kwargs)

    if models.storage_t != 'db':
        @property
        def likes(self):
            """"""
            from models.Likes import Likes
            likes_list = []
            all_likes = models.storage.all(LIkes)
            for like in all_likes.values():
                if like.sign_id == self.id:
                    likes_list.append(like)
            return likes_list
        @property
        def blog(self):
            """"""
            from models.Blog import Blog
            blog_list = []
            all_blog = models.storage.all(Blog)
            for blog in all_blog.values():
                if blog.sign_id == self.id:
                    blog_list.append(blog)
            return blog_list
        
        @property
        def comments(self):
            """"""
            from models.Comments import Comments
            comment_list = []
            all_comments = models.storage.all(Comments)
            for comment in all_comments.values():
                if comment.sign_id == self.id:
                    comments_list.append(comment)
            return comment_list

        @property
        def role(self):
            """"""
            from models.Role import Role
            role_list = []
            all_role = models.storage.all(Role)
            for role in all_role.values():
                if role.sign_id == self.id:
                    role_list.append(role)
            return role_list

        @property
        def specialization(self):
            """"""

            from models.Specialization import Specialization
            specialization_list = []
            all_specialization = models.storage.all(Specialization)
            for specialization in all_specialization.values():
                if specialization.sign_id == self.id:
                    specialization_list.append(specialization)
            return specialization_list

        @property
        def request(self):
            """"""

            from models.Request import Request
            request_list = []
            all_request = models.storage.all(Request)
            for request in all_request.values():
                if request.sign_id == self.id:
                    request_list.append(request)
            return request_list

        @property
        def response(self):
            """"""

            from models.Response import Response
            response_list = []
            all_response = models.storage.all(Response)
            for response in all_response.values():
                if response.sign_id == self.id:
                    response_list.append(response)
            return response_list

        @property
        def points(self):
            """"""

            from models.Points import Points
            points_list = []
            all_points = models.storage.all(Points)
            for point in all_points.values():
                if point.sign_id == self.id:
                    points_list.append(point)
            return points_list

        @property
        def chosen_path(self):
            """"""

            from models.Chosen_Path import ChosenPath
            chosenp_list = []
            all_chosenp = models.storage.all(ChosenPath)
            for chosenp in all_chosenp.values():
                if chosenp.sign_id == self.id:
                    chosenp_list.append(chosenp)
            return chosenp_list

        @property
        def career_path(self):
            """"""

            from models.Career_path import CareerPath
            careerp_list = []
            all_careerp = models.storage.all(CareerPath)
            for careerp in all_careerp.values():
                if careerp.sign_id == self.id:
                    careerp_list.append(careerp)
            return careerp_list

        @property
        def choose_career(self):
            """"""

            from models.Choose_career import ChooseCareer
            career_list = []
            all_career = models.storage.all(ChooseCareer)
            for career in all_career.values():
                if career.sign_id == self.id:
                    career_list.append(career)
            return career_list

        @property
        def comment_likes(self):
            """"""

            from models.Comment_likes import CommentLikes
            clikes_list = []
            all_clikes = models.storage.all(CommentLikes)
            for clikes in all_clikes.values():
                if clikes.sign_id == self.id:
                    clikes_list.append(clikes)
            return clikes_list

