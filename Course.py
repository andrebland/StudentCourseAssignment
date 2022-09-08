import json

class Course:

    def __init__(self, name, startDate, endDate, meetTime, credits, id=-1):
        self.name = name
        self.startDate = startDate
        self.endDate = endDate
        self.meetTime = meetTime
        self.credits = credits
        if id is -1:
            self.id = hash(self)
        else:
            self.id = id
    
    def toJson(self) -> str:
        return json.dumps(self.__dict__)

    def isDateConcurrent(self, otherCourse :'Course'):
        if self.startDate >= otherCourse.startDate and self.startDate <= otherCourse.endDate:
            return True
        if self.endDate <= otherCourse.endDate and self.endDate >= otherCourse.startDate:
            return True
        
        return False


    def isTimeConcurrent(self, otherCourse :'Course'):
        if self.meetTime["day"] != otherCourse.meetTime["day"]:
            return False
        if self.meetTime["start"] >= otherCourse.meetTime["start"] and self.meetTime["end"] <= otherCourse.meetTime["end"]:
            return True
        if self.meetTime["end"] >= otherCourse.meetTime["end"] and self.meetTime["end"] <= otherCourse.meetTime["start"]:
            return True

        return False


    
