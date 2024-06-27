#!/usr/bin/python3
""""""
import uuid
from datetime import datetime
from os import getenv
import sqlalchemy
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class BaseModel:
    """"""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    def __init__(self, *args, **kwargs):
        """"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                        self.__dict__[key] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[key] = value
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
            self.__dict__.update(kwargs)
    def __str__(self):
        """"""
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        if isinstance(dictionary['created_at'], datetime):
            dictionary['created_at'] = self.created_at.isoformat()
        if isinstance(dictionary['updated_at'], datetime):
            dictionary['updated_at'] = self.updated_at.isoformat()
        if "password" in dictionary:
            del dictionary["password"]
        return dictionary
    def delete(self):
        """"""
        
        models.storage.delete(self)
