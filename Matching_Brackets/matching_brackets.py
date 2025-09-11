def is_paired(input_string):
    """
    Check if all types of brackets are correctly paired and nested in the input string.
    The brackets considered are: (), {}, [].

    Args:
        input_string (str): The string to check for matching brackets."""

    new_string = "".join(input_string.split())
    
    brackets = []
    for c in new_string:
        if c == "(" or c == "[" or c == "{":
            brackets.append(c)
        elif c == ")":
            if brackets == [] or brackets [-1] != "(":
                brackets.append(c)
            elif brackets[-1] == "(":
                brackets.pop()
        elif c == "]":
            if brackets == [] or brackets [-1] != "[":
                brackets.append(c)
            elif brackets[-1] == "[":
                brackets.pop()
        elif c == "}":
            if brackets == [] or brackets [-1] != "{":
                brackets.append(c)
            elif brackets[-1] == "{":
                brackets.pop()
        print(brackets)
    return brackets == []


print(is_paired("{[)][]}"))






