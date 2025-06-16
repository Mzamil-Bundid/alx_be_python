import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for the SimpleCalculator class."""

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the addition method with various inputs."""
        self.assertEqual(self.calc.add(2, 3), 5, "2 + 3 should equal 5")
        self.assertEqual(self.calc.add(-1, 1), 0, "-1 + 1 should equal 0")
        self.assertEqual(self.calc.add(0, 0), 0, "0 + 0 should equal 0")
        self.assertEqual(self.calc.add(-5, -3), -8, "-5 + -3 should equal -8")
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0, "1.5 + 2.5 should equal 4.0")

    def test_subtract(self):
        """Test the subtraction method with various inputs."""
        self.assertEqual(self.calc.subtract(5, 3), 2, "5 - 3 should equal 2")
        self.assertEqual(self.calc.subtract(-1, 1), -2, "-1 - 1 should equal -2")
        self.assertEqual(self.calc.subtract(0, 0), 0, "0 - 0 should equal 0")
        self.assertEqual(self.calc.subtract(-5, -3), -2, "-5 - -3 should equal -2")
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0, "5.5 - 2.5 should equal 3.0")

    def test_multiply(self):
        """Test the multiplication method with various inputs."""
        self.assertEqual(self.calc.multiply(2, 3), 6, "2 * 3 should equal 6")
        self.assertEqual(self.calc.multiply(-2, 3), -6, "-2 * 3 should equal -6")
        self.assertEqual(self.calc.multiply(0, 5), 0, "0 * 5 should equal 0")
        self.assertEqual(self.calc.multiply(-2, -3), 6, "-2 * -3 should equal 6")
        self.assertEqual(self.calc.multiply(1.5, 2.0), 3.0, "1.5 * 2.0 should equal 3.0")

    def test_divide(self):
        """Test the division method with various inputs and edge cases."""
        self.assertEqual(self.calc.divide(10, 5), 2.0, "10 / 5 should equal 2.0")
        self.assertEqual(self.calc.divide(-10, 5), -2.0, "-10 / 5 should equal -2.0")
        self.assertEqual(self.calc.divide(0, 5), 0.0, "0 / 5 should equal 0.0")
        self.assertEqual(self.calc.divide(-10, -5), 2.0, "-10 / -5 should equal 2.0")
        self.assertEqual(self.calc.divide(5.0, 2.0), 2.5, "5.0 / 2.0 should equal 2.5")
        self.assertIsNone(self.calc.divide(10, 0), "10 / 0 should return None")

if __name__ == "__main__":
    unittest.main()