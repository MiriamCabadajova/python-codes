def bubble_sort(numbers):
    """
    Implementation of bubble sort algorithm
    :param numbers: array of numbers
    """
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers
