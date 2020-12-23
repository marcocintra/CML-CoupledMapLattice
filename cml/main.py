import matplotlib.pyplot as plt
import CML
import maps
import sys
import numpy as np
import math
from scipy.sparse.linalg import eigs, ArpackError
from matplotlib.colors import LogNorm


def plot(mat):
        plt.clf()
        plt.imshow(mat,cmap=plt.get_cmap('gray'),vmin=0.0,vmax=1.0)
        plt.colorbar()

def plot2(mat):
        plt.clf()
        plt.imshow(mat,cmap=plt.get_cmap('gray'),norm=LogNorm())
        plt.colorbar()


def setMap(mapping):
        if(mapping=='logistic'):
                cmlMap = maps.logisticMap
                par = [extraArg]
        elif(mapping=='onebyf'):
                cmlMap = maps.onebyfMap
                par = sys.argv[-1]
                print("o par do onebyf é: " + par)
                print("\n")
                print("o cmlmap do onebyf é: " + cmlMap)
        return cmlMap, par

if __name__ == "__main__":
        if('-h' in sys.argv) or ('--help' in sys.argv):
                print('================================')
                print('Syntax:')
                print('python main.py commands')
                print('================================')
                print('Commands:')
                print('================================')
                print('-d: display the last iteration of CML')
                print('-mat <type> <matlen>: initial condition type(random or gaussian), matlen(>0)')
                print('-map <map> <parameter>: type of map (logistic or onebyf), parameter is required for both')
                print('-nit <nit>: number of iterations')
                print('-grad <x> <y>: save the gradient from x, y in gradientSeries.csv')
                print('-c coupling: coupling factor(float)')
                print('-o: if set, saves each iteration png files')
                print('-csv: if set, saves each iteration csv files')
                print('-h or --help: display help')
                print('================================')
                exit()
        
        initialMat,matLen,nit,mapping,coupling,neigh,output,nlyap = 'gaussian',128,50,'logistic',0.5,[(1,0),(0,1),(-1,0),(0,-1)],False, 100
        extraArg = 4.0
        for it in range(len(sys.argv)):
                if(sys.argv[it] == '-mat'):
                        if(it+2 < len(sys.argv)):
                                initialMat = sys.argv[it+1]
                                matLen = int(sys.argv[it+2])
                        else:                   
                                raise Exception('Wrong Syntax','-mat')
                elif(sys.argv[it] == '-map'):
                        if(it+1 < len(sys.argv)):
                                mapping=sys.argv[it+1]
                                if mapping=='logistic':
                                        extraArg = round(float(sys.argv[it+2]),5)
                                        if (extraArg>4.0) or (extraArg<0.0):
                                                raise Exception('Wrong Syntax','-map')                                
                        else:
                                raise Exception('Wrong Syntax','-map')
                elif(sys.argv[it] == '-nit'):
                        if(it+1 < len(sys.argv)):
                                nit=int(sys.argv[it+1])
                        else:
                                raise Exception('Wrong Syntax','-nit')
                elif(sys.argv[it] == '-grad'):
                        if(it+2 < len(sys.argv)):
                                x, y = int(sys.argv[it+1]),int(sys.argv[it+2])
                        else:
                                raise Exception('Wrong Syntax','-grad')
                elif(sys.argv[it] == '-c'):
                        if(it+1 < len(sys.argv)):
                                coupling=round(float(sys.argv[it+1]),5)
                        else:
                                raise Exception('Wrong Syntax','-c')
                
        mapCML,par=setMap(mapping)
        grad = []
        if(initialMat=='gaussian') or (initialMat=='random'):
                c = CML.CML(initialMat,matLen)
        else:
                raise Exception('Unknown matrix type')
        
        csumL = []
        csumS = []
        csumM = []
        for i in range(nit):
                if ('-o' in sys.argv):
                        plot(c.mat)
                        plt.savefig('output/images/it'+str(i)+'.png')
                if ('-csv' in sys.argv):
                        with open('output/csv/matrixfile.csv', 'a') as f:
                                np.savetxt(f, c.mat)
                                if(i!=nit-1):
                                       f.write('\n')                                
                if ('-grad' in sys.argv):
                        mod, phase = c.getGradient(x,y)
                        grad.append([mod,phase])
                        np.savetxt('output/gradientSeries.csv',grad,header='mod,phase',comments='',delimiter=',')
                c.getCML(neigh,mapCML,coupling,par)
                        
        if ('-d' in sys.argv):
                plt.figure()
                plot(c.mat)
                plt.figure()
                plot2(c.mat)
                plt.show()
