#!/usr/bin/python3
""" Module: base.py """

from datetime import datetime
import uuid
import models

class BaseModel:
   """Base class for all our classes"""
  
  def __init__(self, *args, **kwargs):
        """ deserialize and serialize a class """
        if kwargs:
            for k, v in kwargs.items():
                if k != '__class__':
                    setattr(self, k, v)
            s = '%Y-%m-%dT%H:%M:%S.%f'
            self.created_at = datetime.strptime(self.created_at, s)
            self.updated_at = datetime.strptime(self.updated_at, s)
        else:
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            self.id = str(uuid.uuid4())
            models.storage.new(self)
  
