def swap_rows(matrix, row1, row2):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]


def reduce_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    rank = min(rows, cols)

    for row in range(rank):
        if matrix[row][row] != 0:
            for i in range(row + 1, rows):
                print(matrix)
                factor = matrix[i][row] / matrix[row][row]
                for j in range(rank):
                    matrix[i][j] -= factor * matrix[row][j]
                    print(matrix)
        else:
            # If the leading coefficient is zero, try to find a row with a non-zero entry in the current column
            non_zero_found = False
            for i in range(row + 1, rows):
                if matrix[i][row] != 0:
                    swap_rows(matrix, row, i)
                    non_zero_found = True
                    break

            if not non_zero_found:
                rank -= 1
                for i in range(rows):
                    matrix[i][row] = matrix[i][rank]

    return rank


# Example usage:
m = [
    [2, 4, 6],
    [1, 2, 3],
    [0, 1, 2]
]

result = reduce_matrix(m)
print("Rank of the matrix is:", result)
