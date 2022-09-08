import unittest
import sys

sys.path.append("..")

from Course import Course


class TestCourse(unittest.TestCase):

    def test_init(self):
        test = Course("trig", 22915, 221215, {"day":"M", "start":4, "end":5}, 5)
        assert(test.name == "trig")
        assert(test.id != -1)
        assert(test.credits == 5)
        assert(test.startDate == 22915)
        assert(test.endDate == 221215)
        assert(test.meetTime == {"day":"M", "start":4, "end":5})

    def test_DateConflictTrue(self):
        trig = Course("trig", 22915, 221215, {"day":"M", "start":4, "end":5}, 5)
        calc = Course("calc", 22915, 221215, {"day":"M", "start":4, "end":5}, 5)

        assert(trig.isDateConcurrent(calc))
    
    def test_DateConflictFalse(self):
        trig = Course("trig", 22915, 221215, {"day":"M", "start":4, "end":5}, 5)
        calc = Course("calc", 22515, 22815, {"day":"M", "start":4, "end":5}, 5)

        assert(not trig.isDateConcurrent(calc))

    def test_TimeConflictTrue(self):
        trig = Course("trig", 22915, 221215, {"day":"M", "start":4, "end":5}, 5)
        calc = Course("calc", 22915, 221215, {"day":"M", "start":4, "end":5}, 5)

        assert(trig.isTimeConcurrent(calc))

    def test_TimeConflictFalse(self):
        trig = Course("trig", 22915, 221215, {"day":"M", "start":4, "end":5}, 5)
        calc = Course("calc", 22915, 221215, {"day":"M", "start":6, "end":7}, 5)
        phys = Course("phys", 22915, 221215, {"day":"W", "start":4, "end":5}, 5)

        assert(not trig.isTimeConcurrent(calc))
        assert(not trig.isTimeConcurrent(phys))


if __name__ == '__main__':
    unittest.main()