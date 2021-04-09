import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import curve_fit

lin=lambda x, b, a : a + x * b


def calibaration(f):
    df = pd.read_excel('lock.xlsx', sheet_name='calib')
    data = df.dropna()


    vsig = data['Vsig'].tolist()
    v500 = data[f'Vdc({f}Hz.)'].tolist()

    print(vsig)
    print(v500)

    pov,pocv = curve_fit(lin,vsig, v500)

    plt.plot(vsig, v500, "ro", ls='-', label="Data", markersize="10", linewidth = "1.3")
    x = np.linspace(65, 300)
    plt.plot(x, lin(x, *pov), label="Fit", c="black", linewidth="2.5" )
    plt.legend(shadow=True, ncol=2, loc="best").set_draggable(True)
    plt.xlabel(r"$V_{sig}(\mu Volt.)$", size="14")
    plt.ylabel(r"$V_{DC}(Volt.)$", size="14")
    plt.title(r"Calibration for  $f= %d Hz.$" %(f), size="14")
    plt.text(150, 0.2, "Slope = {0} +/- {2}".format(*np.round(pov*1e6, 3), *np.round(np.sqrt(np.diag(pocv))*1e6, 3)), size="12")
    plt.grid()
    plt.show()


i = 500

while i <= 3000:
    calibaration(i)
    print(i)
    i += 500
