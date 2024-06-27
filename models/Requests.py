#!/usr/bin/python3
""""""

import models
from os import getenv
import sqlalchemy
from sqlalchemy.orm import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel, Base

class Requests(BaseModel, Base):
    """"""

    if models.storage_t == 'db':
        sign_id = Column(String(60), ForeignKey("sign.id"), nullable=False)
        role_id = Column(String(60), ForeignKey("role.id"), nullable=False)
        request = Column(String(200), nullable=False)
        specialization_id = Column(String(60), ForeignKey("specialization.id"), nullable=False)
        response = relationship("Response", backref="request")
    else:
        sign_id = ""
        role_id = ""
        specialization_id = ""
        request = ""

    def __init__(self, *args, **kwargs):
        """"""
        super().__init__(self, *args, **kwargs)

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
