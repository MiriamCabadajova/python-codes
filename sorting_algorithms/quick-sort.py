def partition(array, low, high):
    """
    Partition for quicksort
    :param array: array of numbers
    :param low: lower boundary of interval
    :param high: upper boundary of interval
    """
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            swap(array, i, j)
    swap(array, i + 1, high)


def quick_sort(array, i, j):
    """
    Quick sort in place
    :param array: array of numbers
    :param i: lower boundary of interval
    :param j: upper boundary of interval
    """
    if i < j:
        partition(array, i, j)
        quick_sort(array, i, j - 1)
        quick_sort(array, i + 1, j)
