def flatten(iterable):
    flattened_array = []
    for element in iterable:
        if isinstance(element,list):
            flattened_array.extend(flatten(element))
        else:
            flattened_array.append(element)
    return flattened_array


print(flatten([0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2]))