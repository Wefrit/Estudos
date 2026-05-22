def transpose(text):
    lines = text.splitlines()
    if not lines:
        return ""

    num_rows = len(lines)
    max_len = max(len(line) for line in lines)

    transposed = []

    for col_index in range(max_len):
        new_row = ""
        for row_index in range(num_rows):
            if col_index < len(lines[row_index]):
                new_row += lines[row_index][col_index]
            else:
                if any(col_index < len(lines[r]) for r in range(row_index + 1, num_rows)):
                    new_row += " "
                else:
                    new_row += ""
        transposed.append(new_row)

    return "\n".join(transposed)
