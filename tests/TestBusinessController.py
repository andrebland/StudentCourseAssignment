import unittest
import json
import sys

sys.path.append("..")

from BusinessController import BusinessController
from DatabaseController import DatabaseController


testDBController = DatabaseController()
testController = BusinessController(testDBController)

class TestBusinessLogic(unittest.TestCase):

    def test_createStudent(self):
        testData = json.dumps({"name" : "andre"})
        assert(type(testController.createStudent(testData)) == str)


if __name__ == '__main__':
    unittest.main()