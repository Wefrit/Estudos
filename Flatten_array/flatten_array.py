def flatten(iterable):
    flattened_array = []
    for element in iterable:
        if isinstance(element,list) and element != None:
            flattened_array.extend(flatten(element))
        elif element != None:
            flattened_array.append(element)
    return flattened_array
