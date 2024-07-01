#!/usr/bin/python3
""""""

import models
from os import getenv
import sqlalchemy
from models.Response import Response
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel, Base

class StudentPoints(BaseModel, Base):
    """"""

    if models.storage_t == "db":
        __tablename__ = "studentpoints"
        sign_id = Column(String(60), ForeignKey("sign.id"), nullable=False)
        response_id = Column(String(60), ForeignKey("response.id"), nullable=False)
        points = Column(Integer, default=0)
    else:
        sign = ""
        response_id = ""
        points = ""

    def __init__(self, *args, **kwargs):
        """"""

        super().__init__(*args, **kwargs)
