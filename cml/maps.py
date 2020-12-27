import colorednoise as cn
import numpy as np
cont = 0
noises = np.empty((1))

def logisticMap(x, par):
    if(len(par)>0):
        a = par[0]
    else:
        a = 4.0
    return (a * x * (1.0 - x))
  
def onebyfMap(x, beta, grid, nit,snapshot):
    global cont
    global newarr
    print("contador no onebyfMap: "+str(cont))
    beta = int(beta)
    if(cont == 0):
            #print("nit  "+str(nit))
            #print("\n")
            valores = (grid[0]**2)*(nit)*(5)
            #matrizes = int(valores/grid[0]**2)
            #print("matrizes "+str(matrizes))
            #print("\n")
            noises = cn.powerlaw_psd_gaussian(beta, valores)
            noises = ((noises - np.min(noises))/np.ptp(noises)) * 0.1
            #for i in range(matrizes):
            #       temp = cn.powerlaw_psd_gaussian(beta, valores)
            #       temp = ((temp - np.min(temp))/np.ptp(temp)) * 0.1 + x
            #       temp = (temp - np.min(temp))/np.ptp(temp)
            #       #print("newarr "+str(i)+" "+str(newarr))
            #       #print("\n")
            #       newarr = np.append(newarr,temp)
    #print("snapshot "+str(snapshot))
    #print("\n")
    noises[cont] = noises[cont]+x
    noise = noises[cont]
    cont = cont + 1
    if(cont==40):
            print("newarr "+str(noises))
            print("\n")   
    #print("\n")
    #print("parâmetro x: "+str(x))
    #print("\n")
    #print("grid: "+str(grid))
    #print("\n")
    #print("snapshot: "+str(snapshot))
    #print("\n")
    #print("\n")
    #print("\n")
    return noise
