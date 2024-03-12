#!/usr/bin/python3
"""this module defines a base class for
   all models in our hbnb clone
"""

import models
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all models"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance."""
        from models.engine.file_storage import FileStorage
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for ky, val in kwargs.items():
                if ky in ['created_at', 'updated_at']:
                    """Convert strings to datetime objects"""
                    setattr(self, ky, datetime.strptime(val, time_format))
                else:
                    self.__dict__[ky] = val
        else:
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the object."""
        return f"[{self.__class__.__name__}] [{self.id}] {self.__dict__}"

    def save(self):
        """Update the public instance attribute
           updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all
           keys/values of __dict__ of the instance.
        """
        inst_dict = self.__dict__.copy()
        inst_dict['__class__'] = self.__class__.__name__
        inst_dict['created_at'] = self.created_at.isoformat()
        inst_dict['updated_at'] = self.updated_at.isoformat()
        return inst_dict
