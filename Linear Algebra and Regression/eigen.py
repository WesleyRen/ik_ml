import numpy as np


def calculate_eigenvalues_and_eigenvectors(matrix):
    try:
        # Calculate eigenvalues and eigenvectors
        eigenvalues, eigenvectors = np.linalg.eig(matrix)

        # Sort eigenvalues and eigenvectors in descending order
        sorted_indices = eigenvalues.argsort()[::-1]
        eigenvalues = eigenvalues[sorted_indices]
        eigenvectors = eigenvectors[:, sorted_indices]

        return eigenvalues, eigenvectors
    except Exception as e:
        return None


# Example usage
if __name__ == "__main__":
    # Define a square matrix A
    A = np.array([[4, -2],
                  [1, 1]])

    eigenvalues, eigenvectors = calculate_eigenvalues_and_eigenvectors(A)

    if eigenvalues is not None:
        print("Eigenvalues:", eigenvalues)
        print("Eigenvectors:")
        for i in range(len(eigenvalues)):
            print("Eigenvalue {}:".format(i + 1))
            print(eigenvectors[:, i])
    else:
        print("Error: Unable to calculate eigenvalues and eigenvectors.")
