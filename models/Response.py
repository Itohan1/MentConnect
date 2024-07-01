#!/usr/bin/python3
""""""

import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel, Base

class Response(BaseModel, Base):
    """"""
    if models.storage_t == 'db':
        __tablename__ = 'response'
        sign_id = Column(String(60), ForeignKey('sign.id'), nullable=False)
        request_id = Column(String(60), ForeignKey('request.id'), nullable=False)
        response = Column(String(200), nullable=False)
        points = relationship("Points", backref="response")
    else:
        sign = ""
        request_id = ""
        response = ""
        points = ""

    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(*args, **kwargs)

    @property
    def points(self):
        """"""
        from models.Points import Points
        point_list = []
        all_point = models.storage.all(Points)
        for point in all_point.values():
            if point.response_id == self.id:
                point_list.append(point)
        return point_list
