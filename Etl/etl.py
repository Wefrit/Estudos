def transform(legacy_data):
    new_values = {}
    for score, letters in legacy_data.items():
        for letter in letters:
            new_values[letter.lower()] = score
    return new_values
