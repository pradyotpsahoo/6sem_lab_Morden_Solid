import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import curve_fit


lin=lambda x,b,a : a +x*b
E = lambda x,b,a : a*x**b
ex = lambda x,b,a : a*np.exp(b/x)


def al():
    df = pd.read_excel('four_probe.xlsx', sheet_name='al')
    df.dropna()
    c = np.array(df['c'].tolist())
    v = df['v'].tolist()
    print(df)
    pov,pocv = curve_fit(lin,c,v)
    
    plt.plot(c,v,c='black',ls='',marker='^',label='Data Points', linewidth="1", markersize="9")
    plt.plot(c,lin(c,*pov),c='black',ls='-',label='Fit',linewidth='2')
    plt.text(75, 0.01, "Slope=%0.3e+/-%0.3e"%(pov[0],pocv[0][0]**0.5), size="12")
    plt.title(r"Graph between $V$ vs. $I$ for $Al$",size="16")
    plt.ylabel(r"V$(mVolt.)$",size="14")
    plt.xlabel(r"I$(mA.)$",size="14")
    plt.legend()
    plt.grid()

    plt.show()


def si():
    df = pd.read_excel('four_probe.xlsx', sheet_name='si')
    df.dropna()
    c = np.array(df['c'].tolist())
    v = df['v'].tolist()
    pov,pocv = curve_fit(lin,c,v)
    
    plt.plot(c,v,c='black',ls='',marker='s',label='Data Points', linewidth="1", markersize="9")
    plt.plot(c,lin(c,*pov),c='black',ls='-',label='Fit',linewidth="2")
    plt.text(0.65,40,"Slope=%0.3e+/-%0.3e"%(pov[0],pocv[0][0]**0.5),size="12")
    plt.legend()
    plt.title(r"Graph between $V$ vs. $I$ for $Si$",size="16")
    plt.ylabel(r"V$(mVolt.)$",size="14")
    plt.xlabel(r"I$(mA.)$",size="14")
    plt.grid()
    plt.show()


def ge():
    df = pd.read_excel('four_probe.xlsx', sheet_name='ge')
    df.dropna()
    c = np.array(df['tK'].tolist())[1:]
    v = df['rho_Ex'].tolist()[1:]
    pov,pocv = curve_fit(ex,c,v,maxfev=2000)
    t=np.linspace(353,473,500)
    plt.plot(c,v,c='black',ls='',marker='o',label='Data Points',markersize="9")
    plt.plot(t,ex(t,*pov),c='black',ls='-',label='Fit')
    plt.text(390, 0.042, "A=%0.3e +/- %0.3e\nb=%0.3e +/- %0.3e"%(pov[1],pocv[1][1]**0.5,pov[0],pocv[0][0]**0.5),size=12)
    plt.xlabel("T (K)",size=14)
    plt.ylabel(r"$\rho (\Omega m)$",size=14)
    plt.title(r"Graph between $T(K)$ vs. $\rho(\Omega m)$ for $Ge$",size="16")
    plt.legend()
    plt.grid()
    plt.show()


#al()
#si()
ge()
