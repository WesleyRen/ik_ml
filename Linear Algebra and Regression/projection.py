import numpy as np


def projection(v1, v2):
    vector1 = np.array(v1)
    vector2 = np.array(v2)
    part1 = np.divide(np.dot(vector1, vector2), np.dot(vector2, vector2))
    return np.multiply(part1, vector2)


if __name__ == "__main__":
    a = [1, 2]
    b = [2, 1]
    print(projection(a, b))












