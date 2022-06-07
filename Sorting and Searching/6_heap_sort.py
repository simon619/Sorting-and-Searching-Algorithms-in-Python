def heapify(List, n, pointer):
    largest = pointer
    left = 2 * pointer + 1
    right = 2 * pointer + 2
    if left < n and List[pointer] < List[left]:
        largest = left

    if right < n and List[largest] < List[right]:
        largest = right

    if largest != pointer:
        List[largest], List[pointer] = List[pointer], List[largest]
        heapify(List, n, largest)


def heap_sort(List):
    n = len(List)
    for i in range(n - 1, -1, -1):
        heapify(List, n, i)  # This Creates Max Heap-

    for i in range(n - 1, 0, -1):
        List[0], List[i] = List[i], List[0]
        heapify(List, i, 0)  # This sorts the max Heap

    return List


if __name__ == '__main__':
    list = [10, 56, 70, 8, 2, 97]
    print(f'The List is: {list}')
    print(f'Heap Sorted To: {heap_sort(list)}')
