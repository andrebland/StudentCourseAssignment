from AbstractBusinessController import AbstractBusinessController
from AbstractDatabaseController import AbstractDatabaseController
from threading import Lock
from Course import Course

class BusinessController(AbstractBusinessController):
    def __init__(self, controller :AbstractDatabaseController):
        self.db = controller
        self.mutex = Lock()

    def createStudent(self, student :dict):
        self.mutex.acquire()
        studentID = student["id"]
        ret = self.db.studentInsert(studentID, student)
        self.mutex.release()
        return ret

    def updateStudent(self, studentID :int, updatedStudent :dict):
        self.mutex.acquire()
        ret = self.db.studentUpdate(studentID, updatedStudent)
        self.mutex.release()
        return ret

    def createCourse(self, course :dict):
        self.mutex.acquire()
        id = course["id"]
        ret = self.db.courseInsert(id, course)
        self.mutex.release()
        return ret

    def updateCourse(self, courseID :int, updatedCourse :dict):
        self.mutex.acquire()
        ret =  self.db.courseUpdate(courseID, updatedCourse)
        self.mutex.release()
        return ret

    def addStudentToCourse(self, studentID :int, courseID :int):
        self.mutex.acquire()
        courses = self.db.studentGetCourses(studentID)
        courseToAdd = self.db.courseGet(courseID)
        if courseToAdd is None:
            self.mutex.release()
            return None

        newCourse = Course(courseToAdd["name"], courseToAdd["startDate"], courseToAdd["endDate"], courseToAdd["meetTime"], courseToAdd["credits"])
        for course in courses:
            currentCourse = Course(course["name"], course["startDate"], course["endDate"], course["meetTime"], course["credits"])
            if currentCourse.isDateConcurrent(newCourse) and currentCourse.isTimeConcurrent(newCourse):
                self.mutex.release()
                return None

        ret =  self.db.courseAddStudent(studentID, courseID)
        self.mutex.release()
        return ret

    def removeStudentfromCourse(self, studentID :int, courseID :int):
        self.mutex.acquire()
        ret =  self.db.courseRemoveStudent(studentID, courseID)
        self.mutex.release()
        return ret

    def calculateCourseAverage(self, courseID :int):
        self.mutex.acquire()
        courseGrades = self.db.courseGetGrades(courseID)

        totalGradePoints = 0.0
        totalStudents = 0
        for grade in courseGrades:
            if (grade >= 0):
                totalGradePoints += grade
                totalStudents += 1

        
        self.mutex.release()
        return totalGradePoints / totalStudents

    def getStudentGrade(self, studentID :int, courseID :int):
        self.mutex.acquire()
        ret =  self.db.studentGetGrade(studentID, courseID)
        self.mutex.release()
        return ret

    def getCoursesOfStudent(self, studentID :int):
        self.mutex.acquire()
        ret =  self.db.studentGetCourses(studentID)
        self.mutex.release()
        return ret

    def getStudentsOfCourse(self, courseID :int):
        self.mutex.acquire()
        ret =  self.db.courseGetStudents(courseID)
        self.mutex.release()
        return ret

    def getStudentGradePointAverage(self, studentID :int):
        self.mutex.acquire()
        grades = self.db.studentGetGrades(studentID)

        totalGradePoints = 0.0
        totalClasses = 0
        for grade in grades:
            if (grade >= 0):
                totalGradePoints += grade
                totalClasses += 1
        
        
        self.mutex.release()
        return totalGradePoints / totalClasses

    def setStudentGradeForCourse(self, studentID :int, courseID :int, grade :int):
        self.mutex.acquire()
        ret = self.db.courseSetStudentGrade(studentID, courseID, grade)
        self.mutex.release()
        return ret
