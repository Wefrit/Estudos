def find(search_list, value):
    """Perform a binary search on a sorted list to find the index of a value.

    :param search_list: list - a sorted list of elements to search.
    :param value: any - the value to search for in the list.
    :return: int - the index of the value in the list, or -1 if not found.
    """
    if value not in search_list:
        raise ValueError("value not in array")
    return search_list.index(value)


print(find([1, 3, 4, 6, 8, 9, 11], 6))