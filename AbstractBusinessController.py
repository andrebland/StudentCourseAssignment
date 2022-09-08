from abc import ABC, abstractmethod

class AbstractBusinessController(ABC):

    @abstractmethod  
    def createStudent():
        pass
    
    @abstractmethod  
    def updateStudent():
        pass

    @abstractmethod  
    def createCourse():
       pass

    @abstractmethod  
    def updateCourse():
        pass

    @abstractmethod  
    def addStudentToCourse():
        pass

    @abstractmethod  
    def removeStudentfromCourse():
        pass

    @abstractmethod  
    def calculateCourseAverage():
        pass
    
    @abstractmethod  
    def getStudentGrade():
        pass

    @abstractmethod  
    def getCoursesOfStudent():
        pass
    
    @abstractmethod  
    def getStudentsOfCourse():
        pass

    @abstractmethod  
    def getStudentGradePointAverage():
        pass
    
    @abstractmethod  
    def setStudentGradeForCourse():
        pass