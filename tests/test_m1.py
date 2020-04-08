import unittest
from m1 import fibbonacci

class TestFibbonacci(unittest.TestCase):
    def test_returns_expected_result(self):
        # Arrange, Act
        result: int = fibbonacci(35)

        # Assert
        self.assertEqual(9227465, result)

if __name__ == "__main__":
    unittest.main()