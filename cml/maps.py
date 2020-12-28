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
    
    #print("contador no onebyfMap: "+str(cont))
    beta = int(beta)
    if(cont == 0):
            #print("cont  "+str(cont))
            #print("\n")
            #print("valores  "+str(valores))
            #print("\n")
            #print("matrizes "+str(matrizes))
            #print("\n")
            #print("valores por iteração "+str(valoresporit))
            #print("\n")
            #noises = ((noises - np.min(noises))/np.ptp(noises)) * 0.1
            #matrixnoises = [[0 for x in range()] for y in range(nit)] 
            #matrixnoises = []
            #noises = cn.powerlaw_psd_gaussian(beta, (nit,valoresporit))  
            # seed random number generator
            #seed(1)
            # create white noise series
            #series = [gauss(0.0, 1.0) for i in range(1000)]
            #s = Series(noises[1])
            #print(s.describe())
            #print("\n")
            #plt.plot(s)
            #plt.savefig('foo.png')
            #print("noises")
            #print("\n")
            #print(noises)
            #print("shape noises")
            #print("\n")
            #print(np.shape(noises))
            #print("\n")
            for i in range(nit):
                    #np.array([1, 2, 3])
                    if (nit==0):
                            matrixnoises = np.array([], dtype=np.int64).reshape(0,valoresporit)
                    else:
                    noises = cn.powerlaw_psd_gaussian(beta, valoresporit)
                    #print(type(noises)
                    matrixnoises = np.vstack([matrixnoises,noises]) 
                    #print("noises" + str(noises))
                    #print("\n")
                    #matriznoises = np.vstack((matrixnoises,noises))                   
                    #print("matrixnoises" + str(matrixnoises))
                    #print("\n")
            #       #print("newarr "+str(i)+" "+str(newarr))
            #       #print("\n")
            #       newarr = np.append(newarr,temp)
    #print(np.shape(matrixnoises))
    #print("\n")
    #print("snapshot "+str(snapshot))
    #print("\n")
    #noises[cont] = noises[cont]+x
    #noise = noises[cont]
    cont = cont + 1
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
