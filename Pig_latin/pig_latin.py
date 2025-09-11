def translate(text):
    vowels = "aeiou"
    special_start = ["xr", "yt"]
    words = text.split()
    result = []

    for word in words:
        if word[0] in vowels or any(word.startswith(r) for r in special_start):
            result.append(word + "ay")
            continue
        idx = 0
        while idx < len(word):
            if word[idx] in vowels or (word[idx] == "y" and idx != 0):
                break
            idx += 1
        if idx > 0 and word[idx-1] == 'q' and idx < len(word) and word[idx] == 'u':
            idx += 1

        result.append(word[idx:] + word[:idx] + "ay")

    return " ".join(result)
