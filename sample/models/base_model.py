#!/usr/bin/python3


import uuid
from datetime import datetime as dt
""" define the BaseModel class """

class BaseModel:
    
    def __init__(self, id=None, created_at=None, updated_at=None):
        """Initialize a new Base. 
        Args: 
            id (int): The identity of the new Base.
        """
        Id = uuid.uuid4()
        genId = str(Id)
        now = dt.now()

        time_formated = dt.isoformat(now)

        self.updated_at = time_formated

        if id is not None:
            self.id = id
        else:
            self.id = genId

        if created_at is not None:
            self.created_at = created_at
        else:
            self.created_at = time_formated


    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

myclass = Base_model()
print(myclass.id)
print(myclass.created_at)
print(myclass.updated_at)
print('--__--__---__--__--__--__ -- __--__ ---__--__--')
print(myclass.__str__())

