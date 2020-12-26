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
  
def onebyfMap(x, beta, grid, snapcont,nit):
    beta = int(beta)
    if(snapcont == 1):
            print("nit  "+str(nit))
            print("\n")
            chamadas = (grid[0]**2)*(nit)*(5)
            for i in range(chamadas):
                    temp = cn.powerlaw_psd_gaussian(beta, (grid[0], grid[1]))
                    temp = ((temp - np.min(temp))/np.ptp(temp)) * 0.1 + x
                    temp = (temp - np.min(temp))/np.ptp(temp)
                    newarr = temp.reshape(-1)
                    print("newarr "+str(i)+" "+str(newarr))
                    print("\n")
            
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
