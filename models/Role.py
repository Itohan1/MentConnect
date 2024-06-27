#!/usr/bin/python3
""""""

import models
from os import getenv
import sqlalchemy
from sqlalchemy.orm import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel, Base

class Role(BaseModel, Base):
    """"""

    if models.storage_t == 'db':
        __tablename__ = "role"
        sign_id = Column(String(60), ForeignKey("sign"), nullable=False)
        role = Column(String(60), nullable)
        request = relationship("Requests", backref="role_request")
        specialization = relationship("Specialization", backref="role_spe")
    else:
        sign_id = ""
        role = ""
        request = ""
        specialization = ""

    def __init__(self, *args, **kwargs):
        """"""

        super().__init__(*args, **kwargs)

    @property
    def request(self):
        """"""
        from models.Requests import Requests
        request_list = []
        all_request = models.storage.all(Requests)
        for request in all_request.values():
            if request.role_id == self.id:
                request_list.append(request)
        return request_list

    @property
    def specialization(self):
        """"""
        from models.Specialization import Specialization
        specialization_list = []
        all_specialization = models.storage.all(Requests)
        for specialization in all_specialization.values():
            if specialization.role_id == self.id:
                specialization_list.append(request)
        return specialization_list
