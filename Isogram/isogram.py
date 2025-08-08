def is_isogram(string):
    word = ""
    for letter in string:
        if letter in word:
            return False
        else:
            word += letter
    return True
print(is_isogram("isogram"))  # True
print(is_isogram("hello"))