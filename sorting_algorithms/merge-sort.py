def merge(array, aux, left, mid, right):
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
    if left == right:
        return
    middle = (left + right) // 2

    merge_sort(array, aux, left, middle)
    merge_sort(array, aux, middle + 1, right)

    merge(array, aux, left, middle, right)
