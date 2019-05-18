def my_max(numbers):
    """
    Function which returns maximum in array of numbers
    :param numbers: array of numbers
    :return: maximum number from array
    """
    maximum = 0
    for i in range(len(numbers)):
        if numbers[i] >= maximum:
            maximum = numbers[i]
    return maximum


def nonzero_product(numbers):
    """
    Function which calculates product of non-zero elements in array
    :param numbers: array of numbers
    :return: product of non-zero elements
    """
    result = 1
    for i in range(len(numbers)):
        if numbers[i] != 0:
            result *= numbers[i]
    return result


def flatten(lists):
    """
    Function which flattens list of lists by printing its values
    :param lists: list of lists
    """
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            print(lists[i][j], end=" ")


def count_a(text):
    """
    Function which finds the number of occurrences of 'A' or 'a'
    :param text: input string
    :return: number of a's in a string
    """
    text = list(text)
    counter = 0
    for i in range(len(text)):
        if text[i] == 'A' or text[i] == 'a':
            counter += 1
    return counter


def string_intersection(left, right):
    """
    Function which prints intersection of two strings if there is any
    :param left: first string
    :param right: second string
    """
    left = list(left)
    right = list(right)
    temp = 0
    if len(left) <= len(right):
        temp = len(left)
    else:
        temp = len(right)
    for i in range(temp):
        if left[i] == right[i]:
            print(left[i], end="")


def palindrom(text):
    """
    Function which returns whether the string is palindrome
    :param text: input string
    :return: true / false
    """
    text = list(text)
    a = list(text[::-1])
    return a == text


def caesar(text, klic):
    """
    Implementation of caesar cipher
    :param text: input string
    :param klic: number for the cipher
    """
    text = text.upper()
    for i in range(len(text)):
        a = ord(text[i]) + klic
        if a > 90:
            print(chr(a - 26), end="")
        else:
            print(chr(a), end="")


# caesar("zirafa", 3)


def tuple_reverse(text, n):
    """
    Function which reverses every n characters in a string
    :param text: input string
    :param n: number of characters to be reversed
    """
    x = n
    i = 0
    while i < len(text):
        a = text[i:n]
        print(a[::-1], end="")
        i += x
        n += x
