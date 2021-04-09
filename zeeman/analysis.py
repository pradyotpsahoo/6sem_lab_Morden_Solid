import matplotlib.pylab as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

lin = lambda x,a,b: a*x +b


def plot_it():

    #fr_range = [16.25,15.3,14.37,13.36,12.49]
        df = pd.read_excel("zeeman.xlsx",sheet_name='Sheet1')
        df=df.dropna(subset=['B', 'Dk'])
        print(df)
        b = np.array(df['B'].tolist())
        dk=np.array(df['Dk'].tolist())
    #pointers = ['^','o','d','P','*']
    #colors = ['#F57C12','#143C24','#031521','#CA4286','#607E4D']
    
        plt.plot(b, dk,c='brown',marker='o',ls='-',label='Data points', mfc='red', ms="11", lw=0.5 )
        pov,pocv = curve_fit(lin,b,dk)
        plt.xlabel("B(mT)",size=14)
        plt.ylabel(r"$\Delta k(m^{-1})$",size=14)
        plt.plot(b,lin(b,*pov),color='#143C24',ls='-',label='Fit', lw='2')
        plt.title('Graph between $\Delta k\ vs\ B $', size=14)
        text = "Slope = %0.2e +/- %0.2e\nIntercept = %0.2e +/- %0.2e"%(pov[0],pocv[0][0]**0.5,pov[1],pocv[1][1]**0.5)
        plt.text(440, 40, text, size=11)
        plt.yticks(rotation=0)
        plt.xticks(rotation=0)
        plt.grid()
        plt.legend()
        plt.savefig("plot.png")
        plt.show()
        #plt.clf()
plot_it()
