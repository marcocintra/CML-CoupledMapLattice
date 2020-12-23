import colorednoise as cn
import numpy as np
cont = -1

def logisticMap(x, par):
    if(len(par)>0):
        a = par[0]
    else:
        a = 4.0
    return (a * x * (1.0 - x))
  
def onebyfMap(u, beta):
    temp = cn.powerlaw_psd_gaussian(beta, (u.shape[0], u.shape[1]))
    temp = ((temp - np.min(temp))/np.ptp(temp)) * 0.1 + u
    temp = (temp - np.min(temp))/np.ptp(temp)
    print(temp)
    return temp
