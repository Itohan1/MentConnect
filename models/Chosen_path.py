#!/usr/bin/python3
""""""

import models
from os import getenv
import sqlalchemy
from sqlalchemy.orm import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel, Base

class ChosenPath(BaseModel):
    """"""

    if models.storage_t = "db":
        sign_id = Column(String(60), ForeignKey('sign.id'), nullable=False)
        careerpath_id = Column(String(60), ForeignKey('careerpath.id'), nullable=False)
        role_id = Column(String(60), ForeignKey('role.id'), nullable=False)
        choose_id = Column(String(60), ForeignKey('choose.id'), nullable=False)
        career_name = Column(String(200), nullable=False)
    else:
        sign_id = ""
        role_id = ""
        careerpath_id = ""
        choose_id = ""
        career_name = ''

    def __init__(self, *args, **kwargs):
        """"""

        super().__init__(*args, **kwargs)

