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
    def __init__(self, status_code):
        self.status_code = status_code


class TestStudentCourseAssignemnt(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()