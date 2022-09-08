from abc import ABC, abstractmethod

class AbstractDatabaseController(ABC):

    @abstractmethod    
    def courseInsert():
        pass

    @abstractmethod
    def courseUpdate():
        pass

    @abstractmethod
    def courseAddStudent():
        pass

    @abstractmethod
    def courseRemoveStudent():
        pass

    @abstractmethod
    def courseSetStudentGrade():
        pass

    @abstractmethod
    def courseGetStudents():
        pass

    @abstractmethod
    def courseGetGrades():
        pass

    @abstractmethod
    def courseGet():
        pass


    @abstractmethod
    def studentInsert():
        pass

    @abstractmethod
    def studentUpdate():
        pass

    @abstractmethod
    def studentGetCourses():
        pass

    @abstractmethod
    def studentGetGrades():
        pass

    @abstractmethod
    def studentGetGrade():
        pass



