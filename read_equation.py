import numpy as np

def readfile(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()
    return content


def convert_content_to_array(content):

    matrix_list = []
    vector = None
    state = None
    valid_states = {'A': matrix_list, 'b': 'vector'}

    for line in content:
        line = line.strip()

        if not line:
            continue
        # Parse prefixes to identify matrix 'A' and vector 'b'
        if line.startswith('A:') or line.startswith('b:'):
            prefix = line.split(':')[0]
            if prefix in valid_states:
                if state == prefix:
                    raise ValueError(f"Duplicate '{prefix}:' encountered.")
                state = prefix
            else:
                raise ValueError(f"Unexpected prefix '{prefix}:' encountered.")
            continue

        # Parse the numbers
        numbers = np.array([float(x) for x in line.split()])
        if state == 'A':
            matrix_list.append(numbers)
        elif state == 'b':
            if vector is not None:
                raise ValueError("Duplicate 'b:' encountered.")
            vector = numbers

    # Check if both matrix and vector were found
    if not matrix_list or vector is None:
        raise ValueError("File must contain both 'A:' and 'b:' sections.")

    # Convert the list of lists to a 2D array
    matrix = np.vstack(matrix_list)
    rows, cols = matrix.shape

# Check if the matrix is square, overdetermined or underdetermined
    if rows > cols:
        raise ValueError("The system of equations is overdetermined.")
    elif rows < cols:
        raise ValueError("The system of equations is underdetermined.")
    elif rows != len(vector) or any(cols != len(row) for row in matrix_list):
        raise ValueError("Inconsistent matrix and vector dimensions.")

    return matrix, vector






