import colorednoise as cn
import numpy as np
import multiprocessing
from concurrent import futures

cont = 0
noises = np.array([])
matrixnoises = np.array([])

def logisticMap(x, par):
    if(len(par)>0):
        a = par[0]
    else:
        a = 4.0
    return (a * x * (1.0 - x))

#def work(beta, size):
#    return np.array(cn.powerlaw_psd_gaussian(beta, size))

#def onebyfMap(x, beta, grid, nit, snapshot):
#    global cont
#    global noises
#    global matrixnoises
#    valores = (grid[0]**2)*(nit)*(5)
#    matrizes = int(valores/grid[0]**2)
#    valoresporit = int(valores/nit)
#    beta = int(beta)
#    if(cont == 0):
#        matrixnoises = np.array([]).reshape(0,valoresporit)
#
#        workers = multiprocessing.cpu_count()
#
#        with futures.ProcessPoolExecutor(workers) as executor:
#            to_do = []
#            for i in range(nit):
#                future = executor.submit(work, beta, valoresporit)
#                future.sid = 'noise snapshot {}'.format(i)
#                to_do.append(future)

#            for future in futures.as_completed(to_do):
                # Para um array com os ruídos de todos os snapshots
#                res = future.result()
#                matrixnoises = np.vstack([matrixnoises, res])
#                print(f'#{future.sid} successfully generated!')

#    indice = cont-(valoresporit*(snapshot+1))
#    cont = cont + 1
#    return matrixnoises[snapshot][indice] + x


def onebyfMap(x, beta, grid, nit,snapshot):
    global cont
    global noises
    global matrixnoises
    valores = (grid**2)*(nit)*(5)
    matrizes = int(valores/grid**2)
    valoresporit = int(valores/nit)
    beta = int(beta)
    if(cont == 0):
            # matrixnoises = np.array([]).reshape(0,valoresporit)
            matrixnoises = []
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
                    #noises = ((noises - np.min(noises))/np.ptp(noises)) * 0.1
                    #print("noises" + str(noises))
                    #print("\n")
                    #print("type noises" + str(type(noises)))
                    #print("\n")
                    #print("shape noises" + str(np.shape(noises)))
                    #print("\n")
                    #matrixnoises = np.vstack([matrixnoises,noises])
                    matrixnoises.append(noises) 
                    #print("iteração "+str(i))
                    #print("\n")
                    #print("matrixnoises" + str(matrixnoises))
                    #print("\n")
                    #print("type matrixnoises" + str(type(matrixnoises)))
                    #print("\n")  
                    #print("shape matrixnoises" + str(np.shape(matrixnoises)))
                    #print("\n")    

            matrixnoises = np.array(matrixnoises)
            # if(i==nit-1):
            #     np.savetxt('matrixnoises.txt', matrixnoises)                      
    # print("contador no onebyfMap: "+str(cont))
    # print("\n")
    #print("snapshot "+str(snapshot))
    #print("\n")
    #print("nit "+str(nit))
    #print("\n")
    indice = cont-(valoresporit*(snapshot+1))
    cont = cont + 1
    #print("\n")
    #print("parâmetro x: "+str(x))
    #print("\n")
    #print("grid: "+str(grid))
    #print("\n")
    #with open("matrixnoises_datasetnoise4.txt") as fp:
    #    for i, line in enumerate(fp):
    #        if(i==snapshot):
    #            a = line.split()[indice]
    #print(a[81919])
    #print(i)
    #return 1
    return matrixnoises[snapshot][indice] + x
