#!/usr/bin/python3
""""""
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel, Base

class Blog(BaseModel, Base):
    """"""

    if models.storage_t == "db":
        __tablename__ = 'blog'
        sign_id = Column(String(60), ForeignKey('sign.id'), nullable=False)
        likes = relationship("Likes", backref="blogs")
        comments = relationship("Comments", backref="blogs")
        blog = Column(String(200), nullable=False)
    else:
        sign_id = ""
        likes = ""
        comments = ""
        blog = ""

    def __init__(self, *args, **kwargs):
        """"""

        super().__init__(self, *args, **kwargs)

    if models.storage_t != "db":
        @property
        def likes(self):
            """"""
            from models.Likes import Likes
            likes_list = []
            all_likes = models.storage.all(Likes)
            for like in all_likes.values():
                if like.blog_id == self.id:
                    likes_list.append(like)
            return likes_list

        @property
        def comments(self):
            """"""
            from models.Comments import Comments
            comments_list = []
            all_comments = models.storage.all(Comments)
            for comment in all_comments.values():
                if comment.blog_id == self.id:
                    comments_list.append(comment)
            return comments_list
