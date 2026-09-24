import unittest

import calc


class AddTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)


class SubtractTest(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(calc.subtract(5, 3), 2)


class MultiplyTest(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(calc.multiply(4, 3), 12)


class DivideTest(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(calc.divide(6, 3), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calc.divide(1, 0)


if __name__ == "__main__":
    unittest.main()
