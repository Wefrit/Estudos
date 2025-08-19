def distance(strand_a, strand_b):

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    else:
        distance = 0
        for letter in range(len(strand_a)):
            if strand_b[letter] != strand_a[letter]:
                distance += 1
    return distance


print(distance("A", "A"))

print(distance("GGACTGAAATCTG", "GGACTGAAATCTG"))

print(distance("GGACGGATTCTG", "AGGACGGATTCT"))