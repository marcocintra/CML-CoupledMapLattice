import colorednoise as cn
import numpy as np
cont = -1

def logisticMap(x, par):
    if(len(par)>0):
        a = par[0]
    else:
        a = 4.0
    print ("o que é essa função que tá no logistic? " + str((a * x * (1.0 - x))))
    print ("\n")
    print ("o que é esse parametro x que tá no logistic? " + str(x))
    print ("\n")
    print (type((a * x * (1.0 - x))))
    print ("\n")
    return (a * x * (1.0 - x))
  
def onebyfMap(u, beta):
    temp = cn.powerlaw_psd_gaussian(beta, (u.shape[0], u.shape[1]))
    temp = ((temp - np.min(temp))/np.ptp(temp)) * 0.1 + u
    temp = (temp - np.min(temp))/np.ptp(temp)
    print ("o que é isso que tá no 1/f noise? " + str(temp))
    print ("\n")               
    print (type(temp))
    print ("\n")               
    return temp
