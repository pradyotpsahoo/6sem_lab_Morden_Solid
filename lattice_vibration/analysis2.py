import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import curve_fit

lin = lambda x, b, a: a + x *b
E = lambda x, b: np.exp(b/x)
ex = lambda x, b, a: a*np.sin((b+x)*np.pi/360)

l = 1e-3
c = 60e-9
c1 = 150e-9


def ac(x):
    a = ((1/c) + (1/c1))/l
    b = 1/(l**2)/c/c1
    #print(((a - (a**2 - (4*(np.sin(x*np.pi/180))**2)*b)**0.5)**0.5)/2/np.pi)
    return ((a - (a**2 - (4*(np.sin(x*np.pi/180))**2)*b)**0.5)**0.5)/2/np.pi


def op(x):
    a = ((1/c) + (1/c1))/l
    b = 1/(l**2)/c/c1
    print(((a + (a**2 - (4*(np.sin(x*np.pi/180))**2)*b)**0.5)**0.5)/2/np.pi)
    return ((a + (a**2 - (4*(np.sin(x*np.pi/180))**2)*b)**0.5)**0.5)/2/np.pi



def mono():
    df = pd.read_excel('data2.xlsx', sheet_name='mono')
    df.dropna()
    f = np.array(df['fc'].tolist())
    th = np.array(df['th1_corrf'].tolist())
    pov, pocv = curve_fit(ex, th, f)
    plt.plot(th, f, c='black', ls='-', marker='o', label='Experimental', linewidth="0.8")
    plt.plot(th, ex(th, *pov), c='#000000', label='Theoretical')

    # plt.plot(c,lin(c,*pov),c='black',ls='-',label='Fit')
    # plt.text(50, 0.005, "Slope = %0.3e +/- %0.3e\nIntercept= %0.3e +/- %0.3e"%(pov[0], pocv[0][0]**0.5, pov[1], pocv[1][1]**0.5), size=13)

    plt.xlabel(r"Phase difference $(\theta ^{\circ})$", size=14)
    plt.ylabel("$frequency (kHz)$", size=14)
    plt.title(r"Graph between $\nu$ vs $\theta$ for mono-atomic")
    plt.legend()
    plt.grid()
    plt.show()


def di():
    df = pd.read_excel('data2.xlsx', sheet_name='di')
    df.dropna()
    f = df['fc2'].tolist()
    th = np.array(df['tf2'].tolist())
    f2 = df['fc3'].tolist()
    th2 = np.array(df['tf3'].tolist())

    x = np.linspace(0, 90)
    y = np.linspace(90, 170)
    # plt.errorbar(x, ac(x)/1000, yerr=ac(x)/10000)
    # plt.errorbar(y, op(y) / 1000, yerr=op(y) / 10000)
    plt.plot(x, ac(x)/1000, c='black', ls='-', label='Theoretical', linewidth="2")
    plt.plot(y, op(y)/1000, c='black', ls='-', linewidth="2")

    plt.plot(th, f, c='black', ls='-', marker='o', label='Acoustical branch', linewidth="0.7")
    plt.plot(th2, f2, c='black', ls='-', marker='^', label='Optical branch', linewidth="0.7")

    # plt.plot(c,lin(c,*pov),c='black',ls='-',label='Fit')
    # plt.text(50, 0.005 "Slope= %0.3e +/- %0.3e\nIntercept= %0.3e +/- %0.3e"%(pov[0],pocv[0][0]**0.5,pov[1],pocv[1][1]**0.5),size=13)

    plt.xlabel(r"Phase difference $(\theta ^{\circ})$", size=14)
    plt.ylabel("frequency $(kHz)$", size=14)
    plt.title(r"Graph between $\nu$ vs $\theta$ for di-atomic")
    plt.legend()
    plt.grid()
    plt.show()

"""

def di_the():
    x = np.linspace(0, 90)
    y = np.linspace(100, 175)
    plt.plot(x, ac(x), c='black', ls='-', label='ac')
    plt.plot(y, op(y), c='red', ls='-', label='op')
    plt.show()


"""


def di2():

    df = pd.read_excel('data2.xlsx', sheet_name='di')
    df.dropna()
    tf = df['tf'].tolist()
    print(tf)
    for i in range(18):
        print(tf[i], "->", ac(tf[i])/1000, "->", i+1)


#mono()
#di()
ac(90)
op(90)