def list_number_counter(l):
    if l == []:
        return 0
    else:
        if l[0]:
            l.pop()
            return 1 + list_number_counter(l)


def list_higher_finder(l):
    if l[1] > list[0]:
        higher = l[1]
    list_higher_finder(list[1:])
    return higher


# list = [1, 2, 3, 4, 5, 6]
# print(list_number_counter(list))

list =[3, 5, 2, 6, 7, 1]
print(list_higher_finder(list))

