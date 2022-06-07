def insertion_sort(L):
    for i in range(1, len(L)):
        pointer = L[i]
        j = i - 1

        while j >= 0 and pointer < L[j]:
            L[j + 1] = L[j]
            j -= 1

        L[j + 1] = pointer

    return L


if __name__ == '__main__':
    list = [10, 56, 70, 8, 2, 97]
    print(f'The List is: {list}')
    print(f'Insertion Sorted To: {insertion_sort(list)}')
