import colorednoise as cn
cont = 1

def doublingMap(x,par):
    if x < 0.5:
        return 2.0 * x
    else:
        return 2.0 * x - 1.0
    
def logisticMap(x, par):
    if(len(par)>0):
        a = par[0]
    else:
        a = 4.0
    return (a * x * (1.0 - x))
    
def kanekoMap(x, par):
    if(len(par)>0):
        a = par[0]
    else:
        a = 4.0
    return (1.0 - a*(x**2.0))

def dkanekoMap(x, par):
    if(len(par)>0):
        a = par[0]
    else:
        a = 4.0
    return -2.0*a*x

def dlogisticMap(x, par):
    if(len(par)>0):
        a = par[0]
    else:
        a = 4.0
    return (a -2.0*a*x) 
    
def somMap(x, par):
    a = par[0]
    b = par[1]
    gamma = 0.8 / (1.0 + a)
    if x < gamma:
        return (a * x + 0.2)
    elif x < 0.8:
        return (x - 0.8) / a + 1.0
    else:
        return (1.0 - x) / b
    
def onebyfMap(x, par):
    y = cn.powerlaw_psd_gaussian(par[0], 2)
    global cont
    print("x:")
    print(x)
    print("par[0]:")
    print(par[0])
    print(cont)
    print("y[0]:")
    print(y[0])
    cont = cont + 1
    #return y[0]
