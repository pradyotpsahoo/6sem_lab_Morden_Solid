import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import curve_fit
import matplotlib.markers as mark

lin = lambda x, b, a: x * b + a


def mut_in(f, i):
    df = pd.read_excel('lock.xlsx', sheet_name='mi')
    data = df.dropna()
    freq = []
    slope = []

    while f <= 1600:
        vac = data['Vac'].tolist()
        vdc = data[f'Vdc({f}Hz)'].tolist()

        pov, pocv = curve_fit(lin, vac, vdc)
        pointers = ['o', 'D', '^', 'v', 'h', 's', 'p']

        plt.plot(vac, vdc, ls='-',  label=f"f = {f}Hz.", markersize="10", linewidth=".3", marker=pointers[i], markerfacecolor="blue", color="black")
        x = np.linspace(1.4, 4.25)
        plt.plot(x, lin(x, *pov), c="black", linewidth="2")

        # plt.title(r"$for  \ \ %d Hz.$" %(f), size="14")
        # plt.text(3, 0.5, "Slope={0}+/-{2}".format(*np.round(pov, 3), *np.round(np.sqrt(np.diag(pocv)), 4)), size="12")
        print(f"{f} :- {round(pov[0],3)} +/- {round(pocv[0][0]**0.5,4)}")
        freq.append(f)
        slope.append(pov[0])
        f += 200
        i += 1

    plt.legend(shadow=True, ncol=2, loc="best").set_draggable(True)
    plt.xlabel(r"$V_{AC}(volt.)$", size="14")
    plt.ylabel(r"$V_{DC}(volt.)$", size="14")
    plt.grid()
    plt.show()
    return [freq, slope]


data = mut_in(400, 0)
print(data[0])
print(data[1])
pov, pocv = curve_fit(lin, data[0], data[1])
x = np.linspace(400, 1600)
print(pov[0], pocv[0][0]**0.5)
plt.plot(data[0], data[1], ls="-", label="data", markersize="12", marker="o", markerfacecolor="red", color="blue")
plt.plot(x, lin(x, *pov), color="black", lw="2.5")
plt.ylabel(r"Slope $\alpha$")
plt.xlabel(r"Frequency in $(Hz.)$")
plt.grid()
plt.text(1000, 0.3, "Slope={0:.2E}+/-{1:.2E}".format(pov[0], pocv[0][0]**0.5), size="12")
plt.legend(shadow=True, ncol=2, loc="best").set_draggable(True)
plt.show()
