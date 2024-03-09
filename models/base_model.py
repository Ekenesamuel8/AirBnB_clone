#!/usr/bin/python3

import uuid
from datetime import datetime


class Base:
    def __init__(self, **kwagrs):
        self.__dict__ = kwagrs
        self.id = str(uuid.uuid4().hex)
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at

    def __str__(self):
       # clasname = __class__.__name__
        return f"<{__class__.__name__}> <{self.id}> {self.__dict__}"

a = Base({"eke":"cow"})
print(a)
