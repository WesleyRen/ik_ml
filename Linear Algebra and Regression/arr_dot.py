import numpy as np

'''
a = [
    [1, 2, 3],
    [4, 5, 6],
]

b = [
    [7, 8],
    [9, 10],
    [11, 12],
]

c00 = a00 * b00 + a01 * b10 + a02 * b 20
c01 = a00 * b01 + a01 * b11 + a02 * b 21
c10 = a10 * b00 + a11 * b10 + a12 * b 20
c11 = a10 * b01 + a11 * b11 + a12 * b 21
result: [[c00, c01], [c10, c11]]
'''


def array_dot(matrix_a, matrix_b):
    res = []
    for r in range(len(matrix_a)):
        r_list = []
        for c in range(len(matrix_b[0])):
            prod = 0
            for k in range(len(matrix_b)): # this is also a's column index.
                prod += matrix_a[r][k] * matrix_b[k][c]
            r_list.append(prod)
        res.append(r_list)
    return res


# Example usage
if __name__ == "__main__":
    # Define a square matrix A

    A = [[1, 2, 3], [4, 5, 6]]
    B = [[4, -2],
         [1, 1],
         [2, 3]]
    print(f"dot product is {array_dot(A, B)}")
    out = np.dot(A, B)
    print(f"numpy result: {out}")
