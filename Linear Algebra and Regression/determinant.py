# Q3) Write a Python function to calculate the determinant of a n by n matrix without using Python package
import numpy as np
import copy, math
import unittest


def determinant(m):
    if len(m) == 1:
        return m[0][0]

    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    det = 0
    n = len(m)
    for col in range(n):
        sub_matrix = [row[:col] + row[col + 1:] for row in m[1:]]
        print(f"determinant, sub matrix: {sub_matrix}")
        det += m[0][col] * ((-1) ** col) * determinant(sub_matrix)

    return det


def sub_matrix(a, n):
    '''
    This is much easier to read than above
    '''
    arr = copy.deepcopy(a);

    arr.pop(0)
    for i in range(len(arr)):
        arr[i].pop(n)
    print(arr)
    return arr


def determinant2(m):
    if len(m) == 1:
        return m[0][0]

    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    det = 0
    n = len(m)
    for col in range(n):
        det += m[0][col] * ((-1) ** col) * determinant2(sub_matrix(m, col))

    return det


class Test1(unittest.TestCase):
    m1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
    m2 = [
        [3, 0, 2],
        [2, 0, -2],
        [0, 1, 1]]

    def test(self):
        for matrix in [Test1.m1, Test1.m2]:
            for func in [determinant, determinant2]:
                expected = np.linalg.det(np.array(matrix))
                det = func(matrix)
                print(f"{func.__name__}: {det}, expected:, {expected}")
                self.assertAlmostEquals(det, expected)


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

# if __name__ == "__main__":
#     matrix = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]

#     expected = np.linalg.det(np.array(matrix))

#     det = determinant(matrix)
#     print("Determinant:", det)
#     assert det == expected, f"expected {expected}, but got {det}"
#     det = determinant2(matrix)
#     print("Determinant2:", det)
#     assert det == expected, f"expected {expected}, but got {det}"

#     matrix = [
#         [3, 0, 2],
#         [2, 0, -2],
#         [0, 1, 1]
#     ]

#     expected = np.linalg.det(np.array(matrix))

#     det = determinant(matrix)
#     print("Determinant:", det)
#     assert format(det, '0.2f') == format(expected, 0.2f), f"expected {expected}, but got {det}"
#     det = determinant2(matrix)
#     print("Determinant2:", det)
#     assert format(det, '0.2f') == format(expected, 0.2f), f"expected {expected}, but got {det}"
