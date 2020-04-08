"""
    Chapter 1 problems in the book "Classic Computer Science Problems in Python."
"""
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

    if n in [0, 1]:
        return n

    return fibbonacci(n - 2) + fibbonacci(n - 1)
