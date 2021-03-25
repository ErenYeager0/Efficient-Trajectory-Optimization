import numpy as np

def costFcn(Xc, Uc, D, nS, nU, ww, scale):
    return scale*2

def conEq(Xc, Uc, D, nS, nU, scale, P):
    Xc = Xc.reshape(int(len(Xc)/nS), nS)
    #Uc = Uc.reshape(nU, int(len(Uc)/nU))
    defects = np.dot(D,Xc)/scale
    defects = defects.reshape(-1, 1)

    return defects