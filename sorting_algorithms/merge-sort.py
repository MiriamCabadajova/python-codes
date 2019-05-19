def merge(array, aux, left, mid, right):
    """
    Procedure used in merge sort, array is sorted from left to mid and then from mid + 1 to right
    :param array: input array of integers
    :param aux: auxiliary helper array of 0's, same length as input array
    :param left: left index of array
    :param mid: middle index of array
    :param right: right index of array
    """
    for k in range(left, right + 1):
        aux[k] = array[k]

    i = left
    j = mid + 1

    for k in range(left, right + 1):
        if i > mid:
            array[k] = aux[j]
            j += 1
        elif j > right:
            array[k] = aux[i]
            i += 1
        elif aux[i] <= aux[j]:
            array[k] = aux[i]
            i += 1
        else:
            array[k] = aux[j]
            j += 1


def merge_sort(array, aux, left, right):
    """
    Implementation of merge sort
    :param array: input array of integers
    :param aux: auxiliary helper array of 0's, same length as input array
    :param left: left index of array
    :param right: right index of array
    """
    if left == right:
        return
    mid = (left + right) // 2

    merge_sort(array, aux, left, mid)
    merge_sort(array, aux, mid + 1, right)

    merge(array, aux, left, mid, right)
