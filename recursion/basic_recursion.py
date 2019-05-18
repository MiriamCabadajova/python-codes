def series_sum(n):
    """
    Function which counts series sum
    :param n: the top boundary of series
    """
    if n == 0:
        return 0
    return n + series_sum(n - 1)


def sequence(n):
    """
    Function that counts the sum of sequence
    :param n: sum up to the n-th element
    """
    if n == 0:
        return 5
    else:
        return 2 * sequence(n - 1) - 1


def list_sum(numbers):
    """
    Function which calculates the sum of an array of numbers
    :param numbers: array of numbers
    """
    if len(numbers) == 0:
        return 0

    return numbers[0] + list_sum(numbers[1:])


def hanoi(n, source, target, auxiliary):
    """
    Function which simulates the hanoi tower
    :param n: the number of towers
    :param source: the source tower
    :param target: the target tower
    :param auxiliary: temporary tower
    """
    if n == 0:
        return
    else:
        hanoi(n - 1, source, auxiliary, target)
        print(source, "->", target)
        hanoi(n - 1, auxiliary, target, source)
