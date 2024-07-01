#!/usr/bin/python3
""""""

import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel, Base

class Comments(BaseModel, Base):
    """"""

    if models.storage_t == 'db':
        __tablename__ = "comments"
        sign_id = Column(String(60), ForeignKey('sign.id'), nullable=False)
        blog_id = Column(String(60), ForeignKey('blog.id'), nullable=False)
        comments = Column(String(200), nullable=False)
        comment_like = relationship("CommentLikes", backref="comment")
    else:
        sign_id = ''
        blog_id = ''
        comment = ''
        comment_like = ''

    def __init__(self, *args, **kwargs):
        """"""

        super().__init__(*args, **kwargs)

    @property
    def comment_like(self):
        """"""

        from models.Comment_likes import CommentLikes
        commentlike_list = []
        all_commentlike = models.storage.all(CommentLikes)
        for commentlike in all_commentlike.values():
            if commentlike.comment_id == self.id:
                commentlike_list.append(commentlike)
        return commentlike_list
