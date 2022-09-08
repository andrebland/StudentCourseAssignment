import requests
import json

from typing import List
from Course import Course
from Student import Student

class StudentCourseAssignment:

    def createStudent(self, s :Student) -> bool:
        r = requests.post("http://localhost:1024/api/create_student", json=s.toJson())
        return r.status_code == 200

    def updateStudent(self, s :Student) -> bool:
        r = requests.put("http://localhost:1024/api/update_student", params={"id":s.id}, json=s.toJson())
        return r.status_code == 200

    def createCourse(self, c :Course) -> bool:
        r = requests.post("http://localhost:1024/api/create_course", json=c.toJson())
        return r.status_code == 200
    
    def updateCourse(self, c :Course) -> bool:
        r = requests.put("http://localhost:1024/api/update_course", params={"id":c.id}, json=c.toJson())
        return r.status_code == 200

    def addStudentToCourse(self, s :Student, c :Course) -> bool:
        r = requests.put("http://localhost:1024/api/course_add_student", params={"student_id":s.id, "course_id":c.id})
        return r.status_code == 200

    def removeStudentfromCourse(self, s :Student, c :Course) -> bool:
        r = requests.put("http://localhost:1024/api/course_remove_student", params={"student_id":s.id, "course_id":c.id})
        return r.status_code == 200
    
    def setStudentGradeForCourse(self, s :Student, c :Course, grade :int) -> bool:
        r = requests.put("http://localhost:1024/api/student_set_grade", params={"student_id":s.id, "course_id":c.id, "grade":grade})
        return r.status_code == 200

    def calculateCourseAverage(self, c :Course) -> float:
        r = requests.get("http://localhost:1024/api/course_get_gpa", params={"course_id":c.id})
        res = json.loads(r.content)
        return res

    def getStudentGrade(self, s :Student, c :Course) -> int:
        r = requests.get("http://localhost:1024/api/student_get_grade", params={"student_id":s.id, "course_id":c.id})
        res = json.loads(r.content)
        return res

    def getStudentGradePointAverage(self, s :Student) -> float:
        r = requests.get("http://localhost:1024/api/student_get_gpa", params={"student_id":s.id})
        res = json.loads(r.content)
        return res

    def getCoursesOfStudent(self, s :Student) -> List[Course]:
        r = requests.get("http://localhost:1024/api/student_get_courses", params={"student_id":s.id})
        res = json.loads(r.content)
        courses = []
        for course in res:
            name = course["name"]
            startDate = course["startDate"]
            endDate = course["endDate"]
            meetTime = course["meetTime"]
            credits = course["credits"]
            courses.append(Course(name, startDate, endDate, meetTime, credits))
        return courses

    def getStudentsOfCourse(self, c :Course) -> List[Student]:
        r = requests.get("http://localhost:1024/api/students_in_course", params={"course_id":c.id})
        res = json.loads(r.content)
        students = []
        for student in res:
            name = student["name"]
            creditCapacity = student["creditCapacity"]
            id = student["id"]
            students.append(Student(name, creditCapacity, id))
        return students

