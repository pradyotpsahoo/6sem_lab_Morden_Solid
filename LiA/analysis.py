import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import curve_fit

lin = lambda x, b, a: x * b + a


def mut_in(f):
    df = pd.read_excel('lock.xlsx', sheet_name='mi')
    data = df.dropna()

    vac = data['Vac'].tolist()
    vdc = data[f'Vdc({f}Hz)'].tolist()

    #print(vac)
    #print(vdc)

    pov, pocv = curve_fit(lin, vac, vdc)
    #print(pov)
    #print(pocv)

    plt.plot(vac, vdc, "bo", ls='-', label="Data", markersize="10", linewidth="1.3")
    x = np.linspace(1.4, 4.25)
    plt.plot(x, lin(x, *pov), label="Fit", c="black", linewidth="2.5")
    plt.legend(shadow=True, ncol=2, loc="best").set_draggable(True)
    plt.xlabel(r"$V_{AC}(volt.)$", size="14")
    plt.ylabel(r"$V_{DC}(volt.)$", size="14")
    plt.title(r"$for  \ \ %d Hz.$" %(f), size="14")
    plt.text(3, 0.5, "Slope={0}+/-{2}\nIntercept={1}+/-{3}".format(*np.round(pov, 3), *np.round(np.sqrt(np.diag(pocv)), 3)), size="12")

    plt.grid()
    plt.show()


i = 400

while i <= 1600:
    print(i)
    mut_in(i)
    i += 200


