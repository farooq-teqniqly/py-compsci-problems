import unittest
from pi import calculate_leibniz


class TestGene(unittest.TestCase):
    def calculate_leibniz_returns_expected_result(self):
        # Arrange, Act
        result: float = calculate_leibniz(100000)

        # Assert
        self.assertEqual(3.1415826535897198, result)


if __name__ == "__main__":
    unittest.main()