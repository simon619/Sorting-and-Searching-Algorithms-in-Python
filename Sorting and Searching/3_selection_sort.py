def selection_sort(List):
    pointer = 0
    while pointer < len(List):
        for i in range(pointer, len(List)):
            if List[pointer] > List[i]:
                List[pointer], List[i] = List[i], List[pointer]
        pointer += 1
    return List  # Time Complexity O(n^2)


if __name__ == '__main__':
    list = [10, 56, 70, 8, 2, 97]
    print(f'The List is: {list}')
    print(f'Selection Sorted To: {selection_sort(list)}')
