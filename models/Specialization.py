#!/usr/bin/python3
""""""

import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel, Base

class Specialization(BaseModel, Base):
    """"""

    if models.storage_t == "db":
        __tablename__ = "specialization"
        sign_id = Column(String(60), ForeignKey("sign.id"), nullable=False)
        specialization = Column(String(200), nullable=False) 
    else:
        sign_id = ""
        specialization = ""

    def __init__(self, *args, **kwargs):
        """"""

        super().__init__(*args, **kwargs)
