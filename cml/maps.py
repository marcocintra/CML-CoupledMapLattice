import colorednoise as cn
import numpy as np
cont = 1

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
  
def onebyfMap(x, beta, grid, snapcont):
    beta = int(beta)
    print(str(beta))
    print("\n")
    print(str(type(beta)))
    #print("!!!!!! "+str(grid[0]))
    if(snapcont == 1):
    temp = cn.powerlaw_psd_gaussian(beta, (2, 2))
            temp = ((temp - np.min(temp))/np.ptp(temp)) * 0.1 + x
            temp = (temp - np.min(temp))/np.ptp(temp)
            print("temp...cnapcont==1... "+str(temp))
    #print ("o que é esse u que tá no 1/f noise? " + str(u))
    #print ("\n")               
    #print ("o que é isso que tá no 1/f noise? " + str(temp))
    #print ("\n")               
    #print (type(temp))
    #print ("\n")        
    global cont
    print("contador no onebyfMap: "+str(cont))
    cont = cont + 1
    print("\n")
    print("parâmetro x: "+str(x))
    print("\n")
    print("grid: "+str(grid))
    print("\n")
    print("snapcont: "+str(snapcont))
    print("\n")
    print("\n")
    print("\n")
    return 1 + x
