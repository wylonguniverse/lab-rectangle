import unittest


def area(a, b):
    """Возвращает площадь прямоугольника со сторонами a и b."""
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return a * b


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_rectangle_mul(self):
        res = area(3, 7)
        self.assertEqual(res, 21)

    def test_float_mul(self):
        res = area(2.5, 4)
        self.assertAlmostEqual(res, 10.0)

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            area(-1, 5)


if __name__ == "__main__":
    unittest.main()
