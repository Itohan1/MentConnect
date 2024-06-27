#!/usr/bin/python3
""""""

import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel, Base

class CareerPath(BaseModel, Base):
    """"""
    if models.storage_t == "db":
        __tablename__ = 'careerpath'
        sign_id = Column(String(60), ForeignKey('sign.id'), nullable=False)
        role_id = Column(String(60), ForeignKey('role.id'), nullable=False)
        Career_path = Column(String(200), nullable=False)
        choose_career = Column("Choose_career", backref="career_path")
        chosen_path = Column("Choosen_path", backref="career_path")
    else:
        sign_id = ""
        role_id = ""
        Career_path = ""
        choose_path = ""
        chosen_path = ""

    def __init__(self, *args, **kwargs):
        """"""

        super().__init__(*args, **kwargs)
