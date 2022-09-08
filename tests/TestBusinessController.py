import unittest
import json
import sys
from unittest.mock import patch


sys.path.append("..")

from Course import Course
from BusinessController import BusinessController
from DatabaseController import DatabaseController




class TestBusinessLogic(unittest.TestCase):



    def test_calculateCourseAverage(self):
        with patch("BusinessController.AbstractDatabaseController.courseGetGrades") as mock:
            testDBController = DatabaseController()
            testController = BusinessController(testDBController)
            mock.return_value = [5.0]
            assert(testController.calculateCourseAverage(1) == 5)


    #TODO expand testing


if __name__ == '__main__':
    unittest.main()