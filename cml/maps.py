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
    global noises
    print("contador no onebyfMap: "+str(cont))
    beta = int(beta)
    if(cont == 0):
            #print("cont  "+str(cont))
            #print("\n")
            valores = (grid[0]**2)*(nit)*(5)
            print("valores  "+str(valores))
            print("\n")
            matrizes = int(valores/grid[0]**2)
            print("matrizes "+str(matrizes))
            print("\n")
            valoresporit = int(valores/nit)
            print("valores por iteração "+str(valoresporit))
            print("\n")
            #noises = ((noises - np.min(noises))/np.ptp(noises)) * 0.1
            #matrixnoises = [[0 for x in range()] for y in range(nit)] 
            matrixnoises = []
            noises = cn.powerlaw_psd_gaussian(beta, valoresporit)  
            for k in range(valoresporit):
                    print(noises[k])
            print("shape noises")
            print("\n")
            print(np.shape(noises))
            print("\n")
            '''
            for i in range(nit):
                    noises = cn.powerlaw_psd_gaussian(beta, valoresporit)  
                    row = []
                    for j in range(valoresporit):
                            matrixnoises[i][j] = noises[j]
                    matrixnoises.append(row)        
            #       #print("newarr "+str(i)+" "+str(newarr))
            #       #print("\n")
            #       newarr = np.append(newarr,temp)
            '''
    print(matrixnoises)
    print("\n")
    print(np.shape(matrixnoises))
    print("\n")
    #print("snapshot "+str(snapshot))
    #print("\n")
    #noises[cont] = noises[cont]+x
    #noise = noises[cont]
    '''
    cont = cont + 1
    '''
    #if(cont==40):
    #       print("newarr "+str(noises))
    #       print("\n")   
    #print("\n")
    #print("parâmetro x: "+str(x))
    #print("\n")
    #print("grid: "+str(grid))
    #print("\n")
    #print("snapshot: "+str(snapshot))
    #print("\n")
    #print("\n")
    #print("\n")
    return 1
