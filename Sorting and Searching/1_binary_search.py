def binary_search(L, element, left, right):
    if left == right:
        return L[left] == element

    mid = (left + right) // 2
    if L[mid] == element:
        return True
    elif L[mid] > element:
        if mid == left:
            return False
        else:
            return binary_search(L, element, left, mid - 1)

    else:
        return binary_search(L, element, mid + 1, right)


if __name__ == '__main__':
    x = int(input('Enter a Positive Integer Number: '))
    list = [10, 15, 17, 25, 45, 96]
    print(f'The List is: {list}')
    print(binary_search(list, x, 0, len(list) - 1))
