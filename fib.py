"""
    Chapter 1 problems in the book "Classic Computer Science Problems in Python."
"""
from typing import Dict, Generator
from itertools import count

memo: Dict[int, int] = {0: 0, 1: 1}


def fibbonacci(n: int) -> int:
    """
        Computes the fibbonacci number for the given input number.

        Args:
            n: The number to compute the fibbonacci number for.

        Returns:
            The fibbonacci number.

        Raises:
            ValueError: The input number is less than zero.
    """

    if n < 0:
        raise ValueError("Number cannot be less than zero.")

    if n not in memo:
        memo[n] = fibbonacci(n - 1) + fibbonacci(n - 2)

    return memo[n]


def fibbonacci_sequence() -> Generator[int, None, None]:
    """
        Returns the Fibbonacci sequence.
    Returns:
        A generator containing the Fibbonacci sequence.
    """
    yield 0
    yield 1

    last: int = 0
    next: int = 1

    for _ in count(1):
        last, next = next, last + next
        yield next
