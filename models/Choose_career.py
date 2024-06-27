#!/usr/bin/python3
""""""

import models
from os import getenv
import sqlalchemy
from sqlalchemy.orm import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.basemodel import BaseModel, Base

class ChooseCareer(BaseModel, Base):
    """"""

    if models.storage_t = "db":
        __tablename__ = "choose"
        sign_id = Column(String(60), ForeignKey('sign.id'), nullable=False)
        careerpath = Column(String(60), ForeignKey('careerpath.id'), nullable=False)
        options_name = Column(String(200), nullable)
        chosen_path = Column("ChosenPath", backref="choose_career")
    else:
        sign_id = ""
        careerpath_id = ""
        options_name = ""
        chosen_path = ""

    def __init__(self, *args, **kwargs):
        """"""

        super().__init__(*args, **kwargs)

    def chosen_path(self):
            """"""

            from models.Chosen_career import ChosenCareer
            chosenp_list = []
            all_chosenp = models.storage.all(ChosenPath)
            for chosenp in all_chosenp.values():
                if chosenp.choose_id == self.id:
                    chosenp_list.append(chosenp)
            return chosenp_list
