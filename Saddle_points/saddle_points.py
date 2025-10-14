def saddle_points(matrix):
    row = 0
    column = 0
    for r in range(len(matrix)):
        print(r)    
        for c in matrix[r]:
            if c > row:
                row == c
            print(row)             
    

print(saddle_points([[9, 8, 7], [5, 3, 2], [6, 6, 7]]))