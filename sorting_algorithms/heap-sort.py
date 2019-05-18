class MaxHeap:

    def __init__(self):
        self.size = 0
        self.array = []


def parent_index(i):
    if i > 0:
        return (i - 1) // 2


def left_index(i):
    return 2 * i + 1


def right_index(i):
    return 2 * i + 2


def parent(heap, i):
    if parent_index(i) is not None and parent_index(i) < heap.size:
        return heap.array[parent_index(i)]


def left(heap, i):
    if left_index(i) < heap.size:
        return heap.array[left_index(i)]


def right(heap, i):
    if right_index(i) < heap.size:
        return heap.array[right_index(i)]


def swap(heap, i, j):
    tmp = heap.array[i]
    heap.array[i] = heap.array[j]
    heap.array[j] = tmp


def max_heapify(heap, i):
    tmp = i

    if left(heap, i) is not None:
        if left(heap, i) > heap.array[tmp]:
            tmp = left_index(i)

    if right(heap, i) is not None:
        if right(heap, i) > heap.array[tmp]:
            tmp = right_index(i)

    if tmp != i:
        swap(heap, tmp, i)
        max_heapify(heap, tmp)


def build_max_heap(array):
    heap = MaxHeap()
    heap.array = array
    heap.size = len(array)
    for i in reversed(range(heap.size // 2)):
        max_heapify(heap, i)
    return heap


def extract_max(heap):
    if heap.size == 0:
        return None

    swap(heap, 0, heap.size - 1)
    max_element = heap.array.pop()
    heap.size -= 1

    max_heapify(heap, 0)
    return max_element


def heap_sort(array):
    heap = build_max_heap(array)
    result = []
    while heap.size > 0:
        result.append(extract_max(heap))
    return result


a = [5, 4, 6, 7, 8, 9, 2]
heap1 = build_max_heap(a)
print(heap_sort(a))
