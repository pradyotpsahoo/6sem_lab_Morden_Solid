import matplotlib.pylab as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

lin = lambda x,a,b: a*x +b


def esr():
    fr_range = [16.25,15.3,14.37,13.36,12.49]
    df = pd.read_excel("esr_11.xlsx", sheet_name='sheet')
    df.dropna()
    c = np.array(df['1/i'].tolist())
    pointers = ['^','o','d','P','*']
    colors = ['#077320','#737107','#031521','#720a78','#990511']
    for fr,pointer,color in zip(fr_range,pointers,colors):
    
        q = np.array(df['q_%0.2f'%fr].tolist())
        sig = np.zeros_like(q)+0.5
        plt.errorbar(c, q, yerr=sig, marker=pointer, mfc=color,mec=color, ms=10, mew=1,color=color,linestyle='',label='Data points')
        pov,pocv = curve_fit(lin,c,q,sigma = sig)
        plt.xlabel("1/I($A^{-1}$)", fontsize=12)
        plt.ylabel("Q(mm)", fontsize=12)
        plt.plot(c,lin(c,*pov),color=color,ls='-',label='Fit', lw="2")
        plt.title('Frequency = %0.02fMHz'%fr)
        text = "Slope = {0} +/- {2}\nIntercept = {1} +/- {3}".format(*np.round([*pov,*np.sqrt(np.diag(pocv))],3))
        plt.text(7,q[-2],text)
        plt.grid()
        plt.legend()
        plt.savefig("esrf_%d.png"%fr)
        plt.show()
        plt.clf()

esr()
