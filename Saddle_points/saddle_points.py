def saddle_points(matrix):
    if not matrix:
        return []

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise ValueError("irregular matrix")

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    result = []

    # Percorre cada linha
    for i in range(num_rows):
        max_in_row = max(matrix[i])
        for j in range(num_cols):
            value = matrix[i][j]
            if value == max_in_row:
                column_values = [matrix[k][j] for k in range(num_rows)]
                min_in_column = min(column_values)
                if value == min_in_column:
                    result.append({"row": i + 1, "column": j + 1})

    return result
