import unittest
from src.calculator import add, subtract, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 4), 1)
        self.assertEqual(subtract(1, 2), -1)
        self.assertEqual(subtract(1, 1), 0)
        self.assertEqual(subtract(1, -1), 2)
        self.assertEqual(subtract(5, 0), 5)

    def test_divide(self):
        self.assertEqual(divide(4, 2), 2.0)
        self.assertEqual(divide(10, -5), -2.0)
        self.assertEqual(divide(-8, -2), 4.0)
        self.assertEqual(divide(3, 0), None)

if __name__ == '__main__':
    unittest.main()
