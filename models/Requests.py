#!/usr/bin/python3
""""""

import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel, Base

class Requests(BaseModel, Base):
    """"""

    if models.storage_t == 'db':
        __tablename__ = "request"
        sign_id = Column(String(60), ForeignKey("sign.id"), nullable=False)
        role_id = Column(String(60), ForeignKey("role.id"), nullable=False)
        requests = Column(String(255), nullable=True)
        response = relationship("Response", backref="request")
    else:
        sign_id = ""
        role_id = ""
        specialization_id = ""
        requests = ""

    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(self, *args, **kwargs)

    if models.storage_t != 'db':
        @property
        def response(self):
            """"""

            from models.Response import Response
            response_list = []
            all_response = models.storage.all(Response)
            for response in all_response.values():
                if response.request_id == self.id:
                    response_list.append(response)
            return response_list
