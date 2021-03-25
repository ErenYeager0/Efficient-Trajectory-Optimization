import numpy as np
import unittest
from casadi import *
from scipy.interpolate import interp1d

from chebfun import chebpts
from chebfun import getDifferentiationMatrix
from chebfun import chebpts_dom
from SimpleConstraintFcn import conEq

class FunctionsTestCase(unittest.TestCase):
    def test_chebpts(self):
        print("test_chebpts")
        [x, w, v] = chebpts(10)
        print(x)
        print(w)
        print(v)     
        print("\n")

    def test_difmatrix(self):
        print("test_difmatrix")
        [x, w, v] = chebpts(10)
        D = getDifferentiationMatrix(x, v)
        print(D)
        print("\n")

    def test_chepts_dom(self):
        print("test_chebpts_dom")
        dom = [1, 100]
        t = chebpts_dom(10, dom)
        print(t)
        print("\n")

    def test_inter1d(self):
        print("test_inter1d")
        x = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
        y = np.array([0.0236, 0.0471, 0.0707, 0.0942, 0.1178, 0.1414, 0.1649, 0.1885, 0.2121, 0.2356])
        t = np.array([0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.9])
        f = interp1d(x,y)
        v = f(t)
        print(v)
        print("\n")

    def test_nlp_solvers(self):
        print("test_NLP_solvers")
        x = SX.sym('x')
        y = SX.sym('y')
        z = SX.sym('z')
        nlp = {'x':vertcat(x, y, z), 'f':x**2+100*z**2,'g':z+(1-x)**2-y}
        S = nlpsol('S', 'ipopt', nlp)
        r = S(x0 = [2.5, 3.0, 0.75] ,lbg =0, ubg=0)
        xopt = r['x']
        print('xopt: ', xopt)
        print(S)
        print("\n")

    def test_constraints(self):
        print("test_constraint_functions")
        Xc = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
        nS = 3
        D = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
        scale = 2
        Xc = conEq(Xc, 0, D, nS, 0, 0, scale)
        print(Xc, Xc.dtype)
        print("\n")

unittest.main()
        
        
