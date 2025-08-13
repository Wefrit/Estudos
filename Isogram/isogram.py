def is_isogram(string):
    """
    Determine if a string is an isogram.
    An isogram (Greek: ἰσογράμματον, isogramma, "equal letter") is a word or phrase without a repeating letter.
    Args:
        string (str): The string to evaluate.
    Returns:
        bool: True if the string is an isogram, False otherwise.
    """
    word = ""
    for letter in string.strip().lower():
        if letter in word:
            return False
        elif letter == "-" or letter == " ":
            continue
        else:
            word += letter
    return True
