def transform(legacy_data):
    new_values = {}



dict = {1: ["A", "E"], 2: ["D", "G"]}
new_dict = {}

for score, letters in dict.items():
    print(score, letters)
    for letter in letters:
        new_dict[letter.lower()] = score

print(new_dict)