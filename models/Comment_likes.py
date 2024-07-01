#!/usr/bin/python3
""""""

import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel, Base

class CommentLikes(BaseModel, Base):
    """"""
    if models.storage_t == "db":
        __tablename__ = "comment_likes"
        sign_id = Column(String(60), ForeignKey("sign.id"), nullable=False)
        comment_id = Column(String(60), ForeignKey("comments.id"), nullable=False)
        comment_likes = Column(Integer, default=0)

    else:
        sign_id = ""
        comment_id = ""
        comment_likes = ""

    def __init__(self, *args, **kwargs):
        """"""

        super().__init__(self, *args, **kwargs)
