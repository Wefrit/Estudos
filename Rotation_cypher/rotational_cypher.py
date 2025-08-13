def rotate(text, key):
    """
    Rotates each letter in the text by the given key.
    The rotation is based on the position of the letter in the alphabet, wrapping around if necessary.
    Args:
        text (str): The text to rotate.
        key (int): The number of positions to rotate each letter.
    Returns:
        str: The rotated text.
    """
    rotated_text = []
    for char in text:
        if char.isupper():
            rotated_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            rotated_text.append(rotated_char)
        elif char.islower():
            rotated_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            rotated_text.append(rotated_char)
        else:
            rotated_char = char
            rotated_text.append(rotated_char)
    return ''.join(rotated_text)
        