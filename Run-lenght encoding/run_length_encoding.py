def decode(string):
    pass


def encode(string):
    if not string:
        return ""

    final_list = []
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            if count > 1:
                final_list.append(str(count))
            final_list.append(string[i - 1])
            count = 1

    if count > 1:
        final_list.append(str(count))
    final_list.append(string[-1])

    return "".join(final_list)

print(encode("AAAABC"))