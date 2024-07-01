#!/usr/bin/python3
""""""

import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel, Base

class Likes(BaseModel, Base):
    """"""
    if models.storage_t == "db":
        __tablename__ = "likes"
        sign_id = Column(String(60), ForeignKey("sign.id"), nullable=False)
        blog_id = Column(String(60), ForeignKey("blog.id"), nullable=False)
        likes = Column(Integer, default=0)

    else:
        sign_id = ""
        blog_id = ""
        likes = ""

    def __init__(self, *args, **kwargs):
        """"""

        super().__init__(self, *args, **kwargs)
