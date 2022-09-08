import json

class Student:

    def __init__(self, name, creditCapacity, id=-1):
        self.name = name
        self.creditCapacity = creditCapacity
        if id is -1:
            self.id = hash(self)
        else:
            self.id = id

    def toJson(self) -> str:
        return json.dumps(self.__dict__)

        
    