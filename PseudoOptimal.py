from casadi import *
import chebfun
from numpy import *

class Object:
    def __init__(self):
        self.npts = 0

def timeOptimal(obj):
    print("Initialize optimization problem ... ...")
    roots = chebfun.chebpts(obj.npts)
    return roots


#test
obj = Object()
obj.npts = 12
roots,weights,w = timeOptimal(obj)
print(roots)
print(weights)
print(w)

