import colorednoise as cn
import numpy as np
cont = 0
noises = np.array([])
matrixnoises = np.array([])

def logisticMap(x, par):
    if(len(par)>0):
        a = par[0]
    else:
        a = 4.0
    return (a * x * (1.0 - x))
  
def onebyfMap(x, beta, grid, nit,snapshot):
    global cont
    global noises
    global matrixnoises
    valores = (grid[0]**2)*(nit)*(5)
    matrizes = int(valores/grid[0]**2)
    valoresporit = int(valores/nit)
    beta = int(beta)
    if(cont == 0):
            matrixnoises = np.array([], dtype=np.int64).reshape(0,valoresporit)
            #print("cont  "+str(cont))
            #print("\n")
            #print("valores  "+str(valores))
            #print("\n")
            #print("matrizes "+str(matrizes))
            #print("\n")
            #print("valores por iteração "+str(valoresporit))
            #print("\n")
            for i in range(nit):
                    noises = cn.powerlaw_psd_gaussian(beta, valoresporit)
                    noises = ((noises - np.min(noises))/np.ptp(noises)) * 0.1 + x
                    noises = ((noises - np.min(noises))/np.ptp(noises))
                    print("noises" + str(noises))
                    print("\n")
                    print("type noises" + str(type(noises)))
                    print("\n")
                    print("shape noises" + str(np.shape(noises)))
                    print("\n")
                    matrixnoises = np.vstack([matrixnoises,noises]) 
                    print("matrixnoises" + str(matrixnoises))
                    print("\n")
                    print("type matrixnoises" + str(type(matrixnoises)))
                    print("\n")  
                    print("shape matrixnoises" + str(np.shape(matrixnoises)))
                    print("\n")                    
    print("contador no onebyfMap: "+str(cont))
    print("\n")
    print("snapshot "+str(snapshot))
    print("\n")
    print("nit "+str(nit))
    print("\n")
    indice = cont-(valoresporit*(snapshot+1))
    cont = cont + 1
    #print("\n")
    #print("parâmetro x: "+str(x))
    #print("\n")
    #print("grid: "+str(grid))
    #print("\n")        
    return matrixnoises[snapshot][indice]
