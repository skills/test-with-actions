# System Modules
import sys
import os
import unittest

# Installed Modules
# - None

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci

class TestCalculations(unittest.TestCase):

    def test_area_of_circle_positive_radius(self):
        """Test with a positive radius."""
        # Arrange
        radius = 1

        # Act
        result = area_of_circle(radius)

        # Assert
        self.assertAlmostEqual(result, 3.14159, places=5)

    def test_area_of_circle_zero_radius(self):
        """Test with a radius of zero."""
        # Arrange
        radius = 0

        # Act
        result = area_of_circle(radius)

        # Assert
        self.assertAlmostEqual(result, 0)

    # def test_area_of_circle_negative_radius(self):
    #     """Test with a negative radius to raise ValueError."""
    #     # Arrange
    #     radius = -1

    #     # Act & Assert
    #     with self.assertRaises(ValueError):
    #         area_of_circle(radius)

    def test_get_nth_fibonacci_zero(self):
        """Test with n=0."""
        # Arrange
        n = 0

        # Act
        result = get_nth_fibonacci(n)

        # Assert
        self.assertEqual(result, 0)

    def test_get_nth_fibonacci_one(self):
        """Test with n=1."""
        # Arrange
        n = 1

        # Act
        result = get_nth_fibonacci(n)

        # Assert
        self.assertEqual(result, 1)

    def test_get_nth_fibonacci_ten(self):
        """Test with n=10."""
        # Arrange
        n = 10

        # Act
        result = get_nth_fibonacci(n)

        # Assert
        self.assertEqual(result, 55)

    # def test_get_nth_fibonacci_negative(self):
    #     """Test with a negative number to raise ValueError."""
    #     # Arrange
    #     n = -1

    #     # Act & Assert
    #     with self.assertRaises(ValueError):
    #         get_nth_fibonacci(n)

if __name__ == "__main__":
    unittest.main()
