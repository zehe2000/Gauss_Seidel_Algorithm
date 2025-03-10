import argparse
from read_equation import *
from gauss_seidel_algorithm import *

if __name__ == '__main__':
    # Initialize argparse
    parser = argparse.ArgumentParser(
        description="Solve equations using Gauss-Seidel method.")
    parser.add_argument("file_path",
                        help="Path to the TXT file containing the equations")
    parser.add_argument("-t", "--tolerance", type=float, default=0.0000001,
                        help="Tolerance level for Gauss-Seidel")
    parser.add_argument("-i", "--max_iter", type=int, default=10000,
                        help="Maximum number of iterations for Gauss-Seidel")

    # Parse the arguments
    args = parser.parse_args()

    # Read the equation from file
    equation = readfile(args.file_path)

    # Convert the equation to an array
    matrix, vector = convert_content_to_array(equation)

    # Apply Gauss-Seidel method and print the result
    result = gauss_seidel(matrix, vector, args.tolerance, args.max_iter)

    file = open("output.txt", "x")
    file.write("Solution: " + str(result))
    print(f"The result is {result}")
