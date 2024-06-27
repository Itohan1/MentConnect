#!/usr/bin/python3
""""""

import models
from os import getenv
import sqlalchemy
from sqlalchemy.orm import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel, Base

class Specialization(BaseModel, Base):
    """"""

    if models.storage_t = "db":
        sign_id = Column(String(60), ForeignKey("sign"), nullable=False)
        role_id = Column(String(60), ForeignKey("role"), nullable=False)
        specialization = Column(String(200), nullable=False)

    else:
        sign_id = ""
        role_id = ""
        specialization = ""

    def __init__(self, *args, **kwargs):
        """"""

        super().__init__(*args, **kwargs)
