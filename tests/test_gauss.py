import sys
import os
import numpy.testing as npt

# Ensure Python can find `gauss_seidel_algorithm.py` in the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gauss_seidel_algorithm import *  
import unittest



class testGauss(unittest.TestCase):
    
    def test_determined_equations_1(self):
        matrix = np.array([[6, 4, -1], [2, 5, 1], [-1, -1, 4]])
        vector = np.array([5, 4, -5])
        npt.assert_array_almost_equal(gauss_seidel(matrix, vector, 0.0000001, 10000),
                                      np.array([0, 1, -1]), decimal=7)

#    def test_determined_equations_2(self):
#        matrix = np.array([[2, 1, -1], [1, -1, -1], [2, 2, 1]])
#        vector = np.array([1, 3, 1])
#        npt.assert_array_almost_equal(gauss_seidel(matrix, vector, 0.0000001, 10000),
#                                      np.array([2, -2, 1]), decimal=7)

    def test_determined_equations_3(self):
        matrix = np.array([[4, 1, 0], [1, 4, 1], [0, 1, 4]])
        vector = np.array([15, 10, 5])
        npt.assert_array_almost_equal(gauss_seidel(matrix, vector, 1e-7, 10000),
                                      np.array([95/28, 10/7, 25/28]), decimal=7)

    def test_determined_equations_long(self):
        matrix = np.array([[1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0,
                                                                                1, 0,
                                                                                0, 0,
                                                                                0,
                                                                                0],
                           [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0,
                                                                                0, 0,
                                                                                0, 1,
                                                                                0,
                                                                                0],
                           [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]])
        vector = np.array([5, 7, 8, 2, 1, 5, 10, 9])

        npt.assert_array_almost_equal(gauss_seidel(matrix, vector, 0.0000001, 100),
                                      np.array([5, 7, 8, 2, 1, 5, 10, 9]))

    def test_zero_diagonal(self):
        matrix = np.array([[0, 1], [1, 0]])
        vector = np.array([1, 1])

        with self.assertRaises(ValueError):
            gauss_seidel(matrix, vector, 0.0000001, 100)



if __name__ == "__main__":
    unittest.main()


