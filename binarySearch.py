def binarySearch(list, item):
    lower = 0
    higher = len(list) - 1
    while lower <= higher:
        middle = (lower + higher) // 2  # round down
        guess = list[middle]
        if guess == item:
            return middle
        if guess > item:
            higher = middle - 1
        else:
            lower = middle + 1
    return None


myList = [1, 3, 5, 7, 9]
print(binarySearch(myList, 3))

myList = [1, 3, 5, 7, 9]
print(binarySearch(myList, -1))