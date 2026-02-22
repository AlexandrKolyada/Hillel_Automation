import  unittest
from Work_2 import Circle, Rectangle, Triangle

class TestFigures(unittest.TestCase):

    def test_circle(self):
        circ =Circle(5)
        self.assertAlmostEqual(circ.area(), 78.54, places=2)
        self.assertAlmostEqual(circ.perimeter(), 31.42, places=2)


    def test_triangle_side(self):
        rec = Rectangle(5, 6)
        self.assertEqual(rec.area(), 30)
        self.assertEqual(rec.perimeter(), 22)

    def test_triangle(self):
        trian = Triangle(5, 5, 7)
        self.assertAlmostEqual(trian.area(), 12.5, places=2)
        self.assertEqual(trian.perimeter(), 17)

    def test_circle_negative_value(self):
        with self.assertRaises(ValueError):
            Circle(-5)

    def test_triangle_negative_value(self):
        with self.assertRaises(ValueError):
            Triangle(-5, 5, 7)

    def test_rectangle_negative_value(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 6)




if __name__ == "__main__":
    unittest.main(verbosity=2)