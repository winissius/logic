def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        lower = []
        higher = []
        pivot = array[0]
        for n in array[1:]:
            if n <= pivot:
                lower.append(n)
            if n > pivot:
                higher.append(n)
        return quick_sort(lower) + [pivot] + quick_sort(higher)


list1 = [3, 2, 1, 4, 1, 1, 6, 7, 3, 8, 9, 5]
print(quick_sort(list1))