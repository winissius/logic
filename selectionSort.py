def lowerSearch(array):
    lowest = array[0]
    for n in array:
        if n <= lowest:
            lowest = n
    return lowest


def selectionSort(array):
    sortedArray = []
    while len(array) != 0:
        lower = lowerSearch(array)
        sortedArray.append(lower)
        array.remove(lower)
    return sortedArray


array = [5, 1, 3, 0, 9, 7, 8]
print(lowerSearch(array))
print(selectionSort(array))