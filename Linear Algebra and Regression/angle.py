import numpy as np


def angle(v1, v2):

    # Define two vectors
    vector1 = np.array(v1)
    vector2 = np.array(v2)

    # Calculate the dot product
    dot_product = np.dot(vector1, vector2)

    # Calculate the magnitude of each vector
    magnitude1 = np.linalg.norm(vector1)
    magnitude2 = np.linalg.norm(vector2)

    # Calculate the cosine of the angle between the vectors
    cosine_angle = dot_product / (magnitude1 * magnitude2)

    # Calculate the angle in radians
    angle_rad = np.arccos(cosine_angle)

    # Convert the angle from radians to degrees
    angle_deg = np.degrees(angle_rad)

    print(f"Angle between the vectors (in radians): {angle_rad}")
    print(f"Angle between the vectors (in degrees): {angle_deg}")

    return angle_deg


if __name__ == "__main__":
    # Define a square matrix A

    a = [1, 0]
    b = [1, 1]

    print(f"angle is {angle(a, b)}")

