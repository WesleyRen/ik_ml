def swap_rows(matrix, row1, row2):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]


'''
        [2, 3, 4],
        [3, 2, 1], 
        [4, 7, 8]
        
        [1, 1.5, 2],
        [3, 2, 1], --> factor = 3
        [4, 7, 8]  --> factor = 4
        
        [1, 1.5, 2],
        [1, 2/3, 1/3], 
        [1, 7/4, 8/4] 
        
        [1, 1.5, 2],
        [0, 2/3 - 1.5, 1/3 - 2],  -> factor: 2/3 - 1.5
        [0, 7/4 - 1.5, 8/4 - 2]   -> factor: 7/4 - 1.5
        
'''


def row_echelon(matrix):
    # make a copy.
    a = [row[:] for row in matrix]
    rows, cols = len(a), len(a[0])
    print(a)

    lead = 0
    for r in range(rows):
        if lead >= cols:
            break

        # Find the first non-zero element in the current column
        i = r
        while a[i][lead] == 0:
            i += 1
            if i == rows:
                i = r
                lead += 1
                if lead == cols:
                    break

        # Swap the current row with the row where the leading coefficient is nonzero
        if i != r:
            swap_rows(a, r, i)

        # Scale the row to make the leading coefficient equal to 1
        factor = a[r][lead]
        a[r] = [m / float(factor) for m in a[r]]

        # Eliminate non-zero elements below the leading coefficient
        for r_temp in a:
            print(f"-{r_temp}-")
        print("----------------")

        for i in range(rows):
            if i != r:
                factor = a[i][lead]
                a[i] = [a[i][j] - (factor * a[r][j]) for j in range(cols)]
                for r_temp in a:
                    print(f"-{r_temp}-")
                print("----------------")
        lead += 1

    return a


# Example usage
if __name__ == "__main__":
    # Define a matrix
    a_input = [
        [2, 3, 4],
        [3, 2, 1],
        [4, 7, 8]
    ]

    echelon_matrix = row_echelon(a_input)
    for r_input in echelon_matrix:
        print(r_input)
