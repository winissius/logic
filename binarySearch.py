def binarySearch(list, item):
    lower = 0
    higher = len(list) - 1
    while lower <= higher:
        middle = (lower + higher) / 2 # round down
        guess = list[middle]
        if guess == item:
            return middle
        if guess > item:
            higher = middle - 1
        else:
            lower = middle + 1

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(list) - 1)
lower = 0
higher = len(list) - 1
middle = (lower + higher) // 2
print(middle)