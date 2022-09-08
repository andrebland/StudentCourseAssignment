from AbstractDatabaseController import AbstractDatabaseController
from tinydb import TinyDB, table, where
from tinydb.operations import delete

class DatabaseController(AbstractDatabaseController):
    def __init__(self):
        self.studentDatastore = TinyDB("students.json")
        self.courseDatastore = TinyDB("courses.json")
        self.enrollmentTable = TinyDB("enrollment.json")

    def courseInsert(self, courseID :int, course :dict):
        self.courseDatastore.insert(table.Document(course, doc_id=courseID))
        self.enrollmentTable.insert(table.Document({}, doc_id=courseID))
        return courseID

    def courseUpdate(self, courseID :int, course :dict):
        return self.courseDatastore.update(course, doc_ids=[courseID])

    def courseAddStudent(self, studentID :int, courseID :int):
        return self.enrollmentTable.update({str(studentID) : -1}, doc_ids=[courseID])


    def courseRemoveStudent(self, studentID :int, courseID :int):
        return self.enrollmentTable.update(delete(str(studentID)), doc_ids=[courseID])

    def courseSetStudentGrade(self, studentID :int, courseID :int, grade :int):
        return self.enrollmentTable.update({str(studentID) : grade}, doc_ids=[courseID])

    def courseGetStudents(self, courseID :int):
        course_data = self.enrollmentTable.get(doc_id=courseID)
        result = []
        studentIDs = list(course_data.keys())
        for student in studentIDs:
            result.append(self.studentDatastore.get(doc_id=student))
        return result

    def courseGetGrades(self, courseID :int):
        course_data = self.enrollmentTable.get(doc_id=courseID)
        return list(course_data.values())

    def courseGet(self, courseID :int):
        return self.courseDatastore.get(doc_id=courseID)

    def studentInsert(self, studentID :int, student :dict):
        return self.studentDatastore.insert(table.Document(student, doc_id=studentID))

    def studentUpdate(self, studentID :int, student :dict):
        return self.studentDatastore.update(student, doc_ids=[studentID])

    def studentGetGrades(self, studentID :int):
        courseGrades = self.enrollmentTable.search(where(str(studentID)).exists())
   
        result = []
        for grade in courseGrades:
            result.append(grade[str(studentID)])

        return result
    
    def studentGetCourses(self, studentID :int):
        courses = self.enrollmentTable.search(where(str(studentID)).exists())

        course_list = []
        for document in courses:
            course_list.append(self.courseDatastore.get(doc_id=document.doc_id))
        return course_list

    def studentGetGrade(self, studentID :int, courseID :int):
        courseGrades = self.enrollmentTable.get(doc_id=courseID)
        return courseGrades[str(studentID)]

