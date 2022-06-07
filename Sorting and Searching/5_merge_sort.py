def divide(L):
    if len(L) < 2:
        return L[:]
    else:
        mid = len(L) // 2
        left = divide(L[:mid])
        right = divide(L[mid:])
        return merge_sort(left, right)


def merge_sort(left, right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


if __name__ == '__main__':
    list = [10, 56, 70, 8, 2, 97]
    print(f'The List is: {list}')
    print(f'Merge Sorted To: {divide(list)}')
