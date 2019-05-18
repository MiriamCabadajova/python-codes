def insert_sort(array):
    """
    Insert sort algorithm, sorts the input array so that its elements are sorted in ascending order

    :param array: array of numbers
    :return:
    """
    for i in range(1, len(array)):
        j = i - 1
        key = array[i]
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
