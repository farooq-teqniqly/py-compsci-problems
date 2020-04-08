import unittest
from typing import List
from itertools import islice

from fib import fibbonacci, fibbonacci_sequence


class TestFibbonacci(unittest.TestCase):
    def test_fibbonacci_returns_expected_result(self):
        # Arrange, Act
        result: int = fibbonacci(35)

        # Assert
        self.assertEqual(9227465, result)

    def test_fibbonacci_sequence_returns_expected_result(self):
        # Arrange, Act
        result: List[int] = list(islice(fibbonacci_sequence(), 0, 11))

        # Assert
        self.assertEqual([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55], result)


if __name__ == "__main__":
    unittest.main()
