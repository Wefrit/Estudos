DIGITS = {
    " _ | ||_|   ": "0",
    "     |  |   ": "1",
    " _  _||_    ": "2",
    " _  _| _|   ": "3",
    "   |_|  |   ": "4",
    " _ |_  _|   ": "5",
    " _ |_ |_|   ": "6",
    " _   |  |   ": "7",
    " _ |_||_|   ": "8",
    " _ |_| _|   ": "9",
}


def convert_entry(entry):
    return DIGITS.get(entry, "?")


def convert(input_lines):
    lines = input_lines

    if len(lines) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if any(len(line) % 3 != 0 for line in lines):
        raise ValueError("Number of input columns is not a multiple of three")

    result_lines = []
    for i in range(0, len(lines), 4):
        row_block = lines[i:i + 4]
        num_digits = len(row_block[0]) // 3
        digits = ""
        for j in range(num_digits):
            entry = "".join(line[j * 3:(j + 1) * 3] for line in row_block)
            digits += convert_entry(entry)
        result_lines.append(digits)

    return ",".join(result_lines)
