def bubble_sort(List):
    swap = True
    while swap:
        swap = False
        for i in range(1, len(list)):
            if List[i - 1] > List[i]:
                temp = List[i]
                List[i] = List[i - 1]
                List[i - 1] = temp
                swap = True
    return List  # Time Complexity O(n^2)


if __name__ == '__main__':
    list = [10, 56, 70, 8, 2, 97]
    print(f'The List is: {list}')
    print(f'Bubble Sorted To: {bubble_sort(list)}')
