from chebfun import chebpts
import numpy as np
import unittest

class FunctionsTestCase(unittest.TestCase):
    def test_chebpts(self):
        [x, w, v] = chebpts(10)
        print(x)
        print(w)
        print(v)        
        
unittest.main()
        
        
