import numpy as np

def gauss_seidel(matrix, vector, approx_error, iterationLimit):
    x1 = np.zeros_like(vector, dtype=float)

    for count in range(1, iterationLimit):
        x2 = np.zeros_like(x1, dtype=float)

        for k in range(matrix.shape[0]):
            prod1 = np.dot(matrix[k, :k], x2[:k])
            prod2 = np.dot(matrix[k, k+1:], x1[k+1:])
            if matrix[k, k] == 0:
                raise ValueError("Division by zero")
            x2[k] = (vector[k] - prod1 - prod2) / matrix[k, k]

        if np.allclose(x1, x2, rtol=approx_error):
            break

        x1 = x2

    return x1


