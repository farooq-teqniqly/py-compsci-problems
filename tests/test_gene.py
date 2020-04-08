import unittest
from gene import compress, decompress


class TestGene(unittest.TestCase):
    def test_compress_returns_expected_result(self) -> None:
        # Arrange
        sequence: str = "TAGGGA"

        # Act
        result: int = compress(sequence)

        # Assert
        self.assertEqual(7336, result)

    def test_uncompress_returns_expected_result(self) -> None:
        # Arrange
        bits: int = 7336

        # Act
        result: str = decompress(bits)

        # Assert
        self.assertEqual("TAGGGA", result)

    def test_compress_when_invalid_sequence_raises_ValueError(self):
        # Arrange, Act, Assert
        with self.assertRaises(ValueError):
            result: int = compress("TAGGXTT")