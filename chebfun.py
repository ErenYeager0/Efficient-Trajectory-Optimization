from pychebfun import *
from numpy import *

def chebpts(n):
    dom = [-1,1]
    x = Chebfun.interpolation_points(n) * -1
    x = scaleNodes(x, dom).reshape(-1, 1)
   
    w = quadwts(n)
    w = scaleWeights(w, dom)
    v = barywts(n)

    return x,w,v

def getDifferentiationMatrix(x,v):
    d = [-1, 1]
    n = int(len(x)) 
    D = zeros([n, n])

    for i in range(0, n, 1):
        D[[i], :] = ((v/v[i,0])/(x[i,0]-x)).T
        D[i, i] = 0.
        D[i, i] = -sum(D[i, :])        

    D = 2*D/(d[1] - d[0])

    return D

def barywts(n):
    if n == 0:
        v = []
    elif n == 1:
        v = 1
    else:
        v = ones((n, 1))
        v[n-1, 0]=0.5
        for i in range(n-2, -1, -2):
            v[i,0] = -1.0
        v[0,0] = .5*v[0,0]
    return v

def quadwts(n):
    if n == 0:
        return []
    elif n == 1:
        w = 2
    else:
        # step1: c = 2./[1, 1-(2:2:(n-1)).^2]
        # ugly handle like c
        nn = int(ceil(n/2))
        c = ones((1,nn))
        c[0,0] = 2.
        j = 1
        for i in range(2, n, 2):
            c[0,j] = 2./(1 - i*i)
            j = j + 1
        #print(c)

        #step2:c = [c, c(floor(n/2): -1 : 2)]
        # ugly handle like c
        nnn = int(floor(n/2) - 1) 
        cc = ones((1, nnn + nn))
        j = 0
        for i in range(0, nn, 1):
            cc[0, i] = c[0, i]
            j = j + 1

        for i in range(nnn, 0, -1):
            cc[0, j] = c[0, i]
            j = j + 1
        #print(cc)

        #step3:w = ifft(c)
        w = fft.ifft(cc).real

        #setp4:w([1, n]) = w(1)/2
        w[0,0] = w[0, 0]/2
        w = append(w, w[0,0])
        
    return w

def scaleNodes(x, dom):
    if dom[0] == -1 and dom[1] == 1:
        y = x
        return y
    
    y = dom[1]*(x +1)/2 + dom[0]*(1-x)/2
    return y

def scaleWeights(w, dom):
    if dom[0] == -1 and dom[1] == 1:
        return w
    
    w = (diff(dom)/2)*w
    return w