def is_happy(n: int) -> bool:
    """Happy numbers are defined as those which eventually reach 1 when replaced repeatedly by the sum of the square of their digits. 
    If they loop endlessly in a cycle that does not include 1, then they are not happy numbers.

    :param n: The number to check for happiness
    :return: True if the number is happy, False otherwise

    Example:
    >>> is_happy(7)
    True
    >>> is_happy(45)
    False
    >>> is_happy(1) 
    True
    """
    seen_numbers = {n}
    while n != 1:
        n = sum([int(i) ** 2 for i in str(n)])
        if n in seen_numbers:
            break
        seen_numbers.add(n)
    return n == 1


# Test cases
if __name__ == "__main__":
    assert is_happy(7) == True
    assert is_happy(45) == False
    assert is_happy(1) == True