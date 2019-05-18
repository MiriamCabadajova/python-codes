def maxmin(array, left, right):
    """
    Function which returns maximum and minimum of an array
    :param array: array of integers
    :param left: left index
    :param right: right index
    :return: tuple, first is maximum and then minimum
    """
    if right <= left + 1:
        return max(array[left], array[right]), min(array[left], array[right])
    a, b = maxmin(array, left, (left + right // 2))
    c, d = maxmin(array, ((left + right) // 2) + 1, right)

    return max(a, c), min(b, d)


def reverse_of_string(s):
    """
    Function which reverses a string
    :param s: string
    :return: reverse of a string
    """
    if s == "":
        return s
    else:
        return reverse_of_string(s[1:]) + s[0]


def reverse_of_an_array(array, start, end):
    """
    Function which reverses elements in an array
    :param array: array
    :param start: pointer to start of array
    :param end: pointer to end of array
    """
    if start < end:
        array[start], array[end] = array[end], array[start]
        reverse_of_an_array(array, start + 1, end - 1)


def is_palindrome(s):
    """
    Check whether string is a palindrome
    :param s: string
    :return: true / false
    """
    return len(s) < 2 or s[0] == s[-1] and is_palindrome(s[1:1])


def zipp(a, b):
    """
    Function which zips two strings
    :param a: first array
    :param b: second array
    :return: zipped array
    """
    if not a:
        return b
    elif not b:
        return a
    else:
        return a[0] + b[0] + zipp(a[1:], b[1:])


def count_odd(s):
    """
    Function which sums odd numbers in a list
    :param s: list of numbers
    :return: sum of odd numbers
    """
    if len(s) == 0:
        return 0
    elif s[0] % 2 != 0:
        return s[0] + count_odd(s[1:])
    else:
        return count_odd(s[1:])


def count_even(s):
    """
    Function which sums even numbers in a list
    :param s: list of numbers
    :return: sum of even numbers
        """
    if len(s) == 0:
        return 0
    elif s[0] % 2 == 0:
        return s[0] + count_even(s[1:])
    else:
        return count_even(s[1:])


def median(l):
    """
    Function which finds median of an array
    :param l: array of numbers
    :return: median of an array
    """
    a = len(l)
    if len(l) == 0:
        return 0
    else:
        return (l[0] + median(l[1:])) / a


def binary_search(value, alist):  # O(logn)
    """
    Iterative implementation of binary search
    :param value: searching value
    :param alist:  array of numbers
    :return: true / false
    """
    lower_bound = 0
    upper_bound = len(alist) - 1
    while lower_bound <= upper_bound:
        middle = (lower_bound + upper_bound) // 2
        if alist[middle] == value:
            return True
        elif alist[middle] > value:
            upper_bound = middle - 1
        else:
            lower_bound = middle + 1
    return False


def binary_search_recursive(value, numbers):  # O(logn)
    """
    Recursive implementation of binary search
    :param value: searching value
    :param numbers: array of numbers
    :return: true / false
    """
    middle = numbers[len(numbers) // 2]
    if value == middle:
        return True
    elif value > middle:
        return binary_search_recursive(value, numbers[(len(numbers) // 2):])
    elif value < middle:
        return binary_search_recursive(value, numbers[:(len(numbers) // 2)])
    else:
        return False


def problem_batohu(array, c, weight, i):
    if i == 0:
        return 0
    elif i >= 1 and weight < array[i]:
        return problem_batohu(array, c, weight - array[i], i - 1)
    else:
        return max(c[i] + problem_batohu(arrat, v, weight - array[i], i - 1),
                   problem_batohu(array, v, weight, len(array) - 1))
