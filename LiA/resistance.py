import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import curve_fit

lin = lambda x, b, a: x * b + a


def mut_in(f):
    df = pd.read_excel('lock.xlsx', sheet_name='resistance')
    data = df.dropna()
    vac = data['Vac'].tolist()
    vdc = data[f'Vdc({f}Hz)'].tolist()
    pov, pocv = curve_fit(lin, vac, vdc)
    print(df)
    plt.plot(vac, vdc, "o", ls='-', label="Data", markersize="10", linewidth="0.5", color="green")
    x = np.linspace(1.7, 3.95)
    plt.plot(x, lin(x, *pov), label="Fit", c="black", linewidth="2.5")
    plt.legend(shadow=True, ncol=2, loc="best").set_draggable(True)
    plt.xlabel(r"$V_{AC}(volt.)$", size="14")
    plt.ylabel(r"$V_{DC}(volt.)$", size="14")
    plt.title(r"Calculation of low resistance for $ %d Hz.$" %(f), size="12")
    plt.text(3, 0.75, "Slope={0}+/-{2}".format(*np.round(pov, 3), *np.round(np.sqrt(np.diag(pocv)), 3)), size="12")
    print(f"{f} :- {round(pov[0], 3)} +/- {round(pocv[0][0] ** 0.5, 4)}")

    plt.grid()
    plt.show()
    return pov[0]


i = 200
sum = []
summ = 0
while i <= 800:
    slope = mut_in(i)
    summ += slope
    sum.append(slope)
    i += 200


print(summ/len(sum))
