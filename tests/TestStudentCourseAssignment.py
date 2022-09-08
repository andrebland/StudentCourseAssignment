import unittest
import sys
from unittest.mock import patch

sys.path.append("..")

from StudentCourseAssignment import StudentCourseAssignment
from Course import Course
from Student import Student

test_student = Student("andre", 12)
test_course = Course("calc", "12", "12", {"day" : "M", "start" : 4, "end" : 5}, 4)

class mock_response:
    def __init__(self, status_code=200, content="{}"):
        self.status_code = status_code
        self.content = content

class TestStudentCourseAssignment(unittest.TestCase):

    def test_createStudentSuccess(self):
        with patch("StudentCourseAssignment.requests.post") as mock:
            mock.return_value = mock_response(200)
            test = StudentCourseAssignment()
            testData = Student("Andre", 12)
            assert(test.createStudent(testData))

    def test_createStudentFail(self):
        with patch("StudentCourseAssignment.requests.post") as mock:
            mock.return_value = mock_response(400)
            test = StudentCourseAssignment()
            testData = Student("Andre", 12)
            assert(not test.createStudent(testData))

    def test_createCourseSuccess(self):
        with patch("StudentCourseAssignment.requests.post") as mock:
            mock.return_value = mock_response(200)
            test = StudentCourseAssignment()
            testData = Course("trig", 22915, 221215, {"day":"M", "start":4, "end":5}, 5)
            assert(test.createCourse(testData))

    def test_createCourseFail(self):
        with patch("StudentCourseAssignment.requests.post") as mock:
            mock.return_value = mock_response(400)
            test = StudentCourseAssignment()
            testData = Course("trig", 22915, 221215, {"day":"M", "start":4, "end":5}, 5)
            assert(not test.createCourse(testData))

    def test_updateStudentSuccess(self):
        with patch("StudentCourseAssignment.requests.put") as mock:
            mock.return_value = mock_response(200)
            test = StudentCourseAssignment()
            testData = Student("Andre", 12)
            assert(test.updateStudent(testData))

    def test_updateStudentFail(self):
        with patch("StudentCourseAssignment.requests.put") as mock:
            mock.return_value = mock_response(400)
            test = StudentCourseAssignment()
            testData = Student("Andre", 12)
            assert(not test.updateStudent(testData))

    def test_updateCourseSuccess(self):
        with patch("StudentCourseAssignment.requests.put") as mock:
            mock.return_value = mock_response(200)
            test = StudentCourseAssignment()
            testData = Course("trig", 22915, 221215, {"day":"M", "start":4, "end":5}, 5)
            assert(test.updateCourse(testData))

    def test_updateCourseFail(self):
        with patch("StudentCourseAssignment.requests.put") as mock:
            mock.return_value = mock_response(400)
            test = StudentCourseAssignment()
            testData = Course("trig", 22915, 221215, {"day":"M", "start":4, "end":5}, 5)
            assert(not test.updateCourse(testData))

    def test_removeStudentFromCourseSuccess(self):
        with patch("StudentCourseAssignment.requests.put") as mock:
            mock.return_value = mock_response(200)
            test = StudentCourseAssignment()
            testStudent = Student("Andre", 12)
            testCourse = Course("trig", 22915, 221215, {"day":"M", "start":4, "end":5}, 5)
            assert(test.removeStudentfromCourse(testStudent, testCourse))

    def test_removeStudentFromCourseFail(self):
        with patch("StudentCourseAssignment.requests.put") as mock:
            mock.return_value = mock_response(400)
            test = StudentCourseAssignment()
            testStudent = Student("Andre", 12)
            testCourse = Course("trig", 22915, 221215, {"day":"M", "start":4, "end":5}, 5)
            assert(not test.removeStudentfromCourse(testStudent, testCourse))

    def test_calculateCourseAverage(self):
        with patch("StudentCourseAssignment.requests.get") as mock:
            test = StudentCourseAssignment()
            mock.return_value = mock_response(200, "5.0")
            testCourse = Course("trig", 22915, 221215, {"day":"M", "start":4, "end":5}, 5)
            assert(test.calculateCourseAverage(testCourse) == 5.0)

    def test_getStudentGrade(self):
        with patch("StudentCourseAssignment.requests.get") as mock:
            mock.return_value = mock_response(200, "5.0")
            test = StudentCourseAssignment()
            testStudent = Student("Andre", 12)
            testCourse = Course("trig", 22915, 221215, {"day":"M", "start":4, "end":5}, 5)
            assert(test.getStudentGrade(testStudent, testCourse) == 5.0)

    def test_getStudentGradePointAverage(self):
        with patch("StudentCourseAssignment.requests.get") as mock:
            mock.return_value = mock_response(200, "5.0")
            test = StudentCourseAssignment()
            testStudent = Student("Andre", 12)
            assert(test.getStudentGradePointAverage(testStudent) == 5.0)

    def test_setStudentGradeForCourse(self):
        with patch("StudentCourseAssignment.requests.put") as mock:
            mock.return_value = mock_response(200, "5.0")
            test = StudentCourseAssignment()
            testStudent = Student("Andre", 12)
            testCourse = Course("trig", 22915, 221215, {"day":"M", "start":4, "end":5}, 5)
            assert(test.setStudentGradeForCourse(testStudent, testCourse, 5))

    
    

if __name__ == '__main__':
    unittest.main()