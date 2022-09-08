import unittest
import sys

sys.path.append("..")

from Student import Student


class TestStudent(unittest.TestCase):

    def test_init(self):
        test = Student("Andre", 12)
        assert(test.name == "Andre")
        assert(test.id != -1)
        assert(test.creditCapacity == 12)

    def test_toJson(self):
        test = Student("Andre", 12, 0)
        output = test.toJson()
        assert(output != None)


if __name__ == '__main__':
    unittest.main()