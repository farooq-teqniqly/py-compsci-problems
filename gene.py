"""
Simple string compression.
"""
from typing import Dict


def compress(gene: str) -> int:
    """
    Compresses a gene sequence string.

    Args:
        gene: The sequence to compress.

    Returns:
        An int representing the compressed sequence.
    """
    bit_string: int = 1

    mapping: Dict[str, int] = {
        "A": 0b00,
        "C": 0b01,
        "G": 0b10,
        "T": 0b11
    }

    for nucleotide in gene.upper():
        bit_string <<= 2

        if nucleotide not in mapping:
            raise ValueError(f"Invalid nucleotide '{nucleotide}'.")

        bit_string |= mapping[nucleotide]

    return bit_string


def decompress(compressed_sequence: int) -> str:
    """
        Decompresses a compressed sequence.

        Args:
            compressed_sequence: The sequence to decompress.

        Returns:
            An str representing the gene sequence.
        """
    uncompressed_str: str = ""

    mapping: Dict[int, str] = {
        0b00: "A",
        0b01: "C",
        0b10: "G",
        0b11: "T"
    }

    for i in range(0, compressed_sequence.bit_length() - 1, 2):
        bits: int = compressed_sequence >> i & 0b11

        if bits not in mapping:
            raise ValueError(f"Invalid sequence '{compressed_sequence}'.")

        uncompressed_str += mapping[bits]

    return uncompressed_str[::-1]
