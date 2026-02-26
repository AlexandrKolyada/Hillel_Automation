import unittest
from Work_3 import Student

class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student("Oleh", "Pit", 21, 87)

    def test_update_average(self):
        self.student.update_average_score(95)
        self.assertEqual(self.student.average_score, 95)

    def test_update_average_limit(self):
        self.student.update_average_score(150)
        self.assertEqual(self.student.average_score, 87)

    def test_update_average_negative(self):
        self.student.update_average_score(-10)
        self.assertGreaterEqual(self.student.average_score, 0)