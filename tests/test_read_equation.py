import sys
import os

# Ensure Python can find `read_equation.py` in the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from read_equation import *  
import unittest

class testReadEquation(unittest.TestCase):

    def test_a_is_missing(self):
        content = readfile(os.path.join(os.path.dirname(__file__), 'broken_txt', 'a_is_missing.txt'))
        with self.assertRaises(ValueError):
            convert_content_to_array(content)

    def test_b_is_missing(self):
        content = readfile(os.path.join(os.path.dirname(__file__), 'broken_txt', 'b_is_missing.txt'))
        with self.assertRaises(ValueError):
            convert_content_to_array(content)

    def test_different_row_len(self):
        content = readfile(os.path.join(os.path.dirname(__file__), 'broken_txt', 'different_row_len.txt'))
        with self.assertRaises(ValueError):
            convert_content_to_array(content)

    def test_false_format(self):
        content = readfile(os.path.join(os.path.dirname(__file__), 'broken_txt', 'false_format.txt'))
        with self.assertRaises(ValueError):
            convert_content_to_array(content)

    def test_letters_in_matrix(self):
        content = readfile(os.path.join(os.path.dirname(__file__), 'broken_txt', 'letters_in_matrix.txt'))
        with self.assertRaises(ValueError):
            convert_content_to_array(content)

    def test_two_matrices(self):
        content = readfile(os.path.join(os.path.dirname(__file__), 'broken_txt', 'two_matrices.txt'))
        with self.assertRaises(ValueError):
            convert_content_to_array(content)

    def test_vector_is_missing(self):
        content = readfile(os.path.join(os.path.dirname(__file__), 'broken_txt', 'vector_is_missing.txt'))
        with self.assertRaises(ValueError):
            convert_content_to_array(content)

    def test_underdetermined_equations(self):
        content = readfile(os.path.join(os.path.dirname(__file__), 'broken_txt', 'underdetermined_matrix.txt'))
        with self.assertRaises(ValueError):
            convert_content_to_array(content)

    def test_overdetermined_equations(self):
        content = readfile(os.path.join(os.path.dirname(__file__), 'broken_txt', 'overdetermined_matrix.txt'))
        with self.assertRaises(ValueError):
            convert_content_to_array(content)

if __name__ == "__main__":
    unittest.main()

