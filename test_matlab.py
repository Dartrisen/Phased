from test_python import TestPython
from scipy import io
import numpy as np
import unittest

class TestMatlab(unittest.TestCase):

    def test(self):
        
        test = TestPython()

        matlab_file = io.loadmat('{}{}_{}'.format(test.path, 'matlab', 'test'))
        matlab = np.array(*matlab_file['matlab'], copy = False)

        python_file = io.loadmat('{}{}_{}'.format(test.path, 'python', 'test'))
        python = np.array(*python_file['python'], copy = False)

        np.testing.assert_array_almost_equal(matlab, python, decimal = 5)

if __name__ == '__main__':

    test = TestMatlab()
    test.test()