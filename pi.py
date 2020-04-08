"""
Pi calculation module.
"""


def calculate_leibniz(number_of_terms: int) -> float:
    """
        Calculate pi using Leibniz's formula.

        Args:
            number_of_terms: The number of terms. More terms results in a more accurate
            value for pi.

        Returns:
            The calculated value for pi.
    """
    pi: float = 0.0
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0

    for _ in range(number_of_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0

    return pi
