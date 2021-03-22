from chebfun import chebpts
from chebfun import getDifferentiationMatrix
import numpy as np
import unittest

class FunctionsTestCase(unittest.TestCase):
    def test_chebpts(self):
        print("test_chebpts\n")
        [x, w, v] = chebpts(10)
        print(x)
        print(w)
        print(v)     

    def test_difmatrix(self):
        print("test_difmatrix\n")
        [x, w, v] = chebpts(10)
        D = getDifferentiationMatrix(x, v)
        print(D)

unittest.main()
        
        
