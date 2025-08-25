def append(list1, list2):
    if list1 == list2 == []:
        return []
    else:
        if list1 == []:
            return list2
        if list2 == []:
            return list1
    return list1 + list2


def concat(lists):
    concat_list =[]
    for list in lists:
        concat_list += list
    return concat_list


def filter(function, list):
    return [n for n in list if function(n)]


def length(list):
    return len(list)


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator


def foldr(function, list, initial):
    accumulator = initial
    for item in reversed(list):
        accumulator = function(accumulator, item)
    return accumulator


def reverse(list):
    if list == []:
        return []
    return [item for item in reversed(list)]

    

print(reverse([1, 3, 5, 7]))