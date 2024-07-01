#!/usr/bin/python3
""""""

import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel, Base

class ChosenPath(BaseModel, Base):
    """"""

    if models.storage_t == "db":
        __tablename__ = "chosenpath"
        sign_id = Column(String(60), ForeignKey('sign.id'), nullable=False)
        career_name = Column(String(200), nullable=False)
    else:
        sign_id = ""
        career_name = ''

    def __init__(self, *args, **kwargs):
        """"""

        super().__init__(*args, **kwargs)

