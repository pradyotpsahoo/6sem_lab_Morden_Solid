import matplotlib.pylab as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

lin = lambda x, a, b: a * x + b


def phase_trans():
    df1 = pd.read_excel("phase_trans.xlsx", sheet_name='heating')
    df1.dropna()
    df2 = pd.read_excel("phase_trans.xlsx", sheet_name='cooling')
    df2.dropna()

    cac1 = np.array(df1['cac'].tolist())
    cdc1 = np.array(df1['cdc'].tolist())
    epac1 = np.array(df1["eps_ac"].tolist())
    epdc1 = np.array(df1["eps_dc"].tolist())
    temp1 = np.array(df1['tc'].tolist())
    cac2 = np.array(df2['cac'].tolist())
    cdc2 = np.array(df2['cdc'].tolist())
    epac2 = np.array(df2["eps_ac"].tolist())
    epdc2 = np.array(df2["eps_dc"].tolist())
    temp2 = np.array(df2['tc'].tolist())

    plt.plot(temp1, cdc1, marker="o", lw="2", c="black", label="DC-capacitance", ms="7", mfc="red")
    plt.plot(temp1, cac1, marker="s", lw="2", c="black", label="AC-capacitance", ms="6", mfc="blue")
    text = r"$T_{curie}$ = " + f'{398}K'
    plt.text(360, 450, text, fontsize="12")
    plt.legend(loc="best")
    plt.xlabel(r"Temperature$(K)$", size=14)
    plt.vlines(398, -100, 1251, ls="dashed", colors="k")
    plt.ylabel(r"Capacitance$(pF)$", size=14)
    plt.ylim(0, 1300)
    plt.title(r"$C$ vs $T$ in increasing $T$", size=16)
    plt.grid()
    plt.savefig("ch.png")
    plt.show()
    plt.clf()

    plt.plot(temp2, cdc2, marker="o", lw="2", c="black", label="DC-capacitance", ms="7", mfc="m")
    plt.plot(temp2, cac2, marker="s", lw="2", c="black", label="AC-capacitance", ms="6", mfc="aqua")
    text = r"$T_{curie}$ = " + f'{398}K'
    plt.text(360, 450, text, fontsize="12")
    plt.legend(loc="best")
    plt.grid()
    plt.xlabel(r"Temperature$(K)$",size=14)
    plt.vlines(398, -100, 1251, ls="dashed", colors="k")
    plt.ylabel(r"capacitance$(pF)$", size=14)
    plt.title(r"$C$ vs $T$ in decreasing $T$", size=16)
    plt.ylim(0, 1300)
    plt.savefig("cc.png")
    plt.show()
    plt.clf()

    plt.plot(temp1, epdc1, marker="o", lw="2", c="black", label="DC-dielectric constant", ms="7", mfc="red")
    plt.plot(temp1, epac1, marker="s", lw="2", c="black", label="AC-dielectric constant", ms="6", mfc="blue")
    plt.legend(loc="best")
    text = r"$T_{curie}$ = " + f'{398}K'
    plt.text(370, 10, text, fontsize="12")
    plt.grid()
    plt.xlabel(r"Temperature$(K)$", size =14)
    plt.vlines(398, 0, 25.12, ls="dashed", colors="k")
    plt.ylim(5, 28)
    plt.ylabel(r" $\epsilon_t/\epsilon$", size=14)
    plt.title(r"$\epsilon_t/\epsilon$ vs $T$ in increasing $T$", size=16)
    plt.savefig("eh.png")
    plt.show()
    plt.clf()

    plt.plot(temp2, epdc2, marker="o", lw="2", c="black", label="DC-dielectric constant", ms="7", mfc="m")
    plt.plot(temp2, epac2, marker="s", lw="2", c="black", label="AC-dielectric constant", ms="6", mfc="aqua")
    plt.legend(loc="best")
    text = r"$T_{curie}$ = " + f'{398}K'
    plt.text(360, 10, text, fontsize="12")
    plt.grid()
    plt.xlabel(r"Temperature$(K)$",size="14")
    plt.vlines(398, 0, 25.12, ls="dashed", colors="k")
    plt.ylabel(r" $\epsilon_t/\epsilon$", size="14")
    plt.ylim(5, 28)
    plt.title(r"$\epsilon_t/\epsilon$ in decreasing $T$", size=16)
    plt.savefig("ec.png")
    plt.show()
    plt.clf()


def para_ele():
    df1 = pd.read_excel("phase_trans.xlsx", sheet_name='heating')
    df1.dropna()
    df2 = pd.read_excel("phase_trans.xlsx", sheet_name='cooling')
    df2.dropna()
    cdc1 = np.array(df1['1/cdc'].tolist())[21:]
    temp1 = np.array(df1['tc'].tolist())[21:]
    cdc2 = np.array(df2['1/cdc'].tolist())[:10]
    temp2 = np.array(df2['tc'].tolist())[:10]

    plt.plot(cdc1, temp1, marker="o", lw="0.8", c="brown", label="data points", ms="10", ls="-", mfc="lightgreen")
    pov1, pocv1 = curve_fit(lin, cdc1, temp1)
    plt.ylabel(r"Temperature$(K)$",size=14)
    plt.xlabel(r"1/capacitance$(pF^{-1})$", size=14)
    plt.plot(cdc1, lin(cdc1, *pov1), color="k", ls='-', label='Fit')
    plt.title(r"$1/C$ vs $T$ in increasing $T$", size=16)
    text = "Slope= %0.3e +/- %0.3e\nIntercept= %0.3e +/- %0.3e" % (pov1[0], pocv1[0][0]**0.5, pov1[1], pocv1[1][1]**0.5)
    plt.text(0.00090,405,text, size=10)
    plt.grid()
    plt.legend()
    plt.savefig("fit1.png")
    plt.show()
    plt.clf()

    plt.plot(cdc2, temp2, marker="o", lw="0.8", c="brown", label="data points", ms="10", ls="-", mfc="orange")
    pov2, pocv2 = curve_fit(lin, cdc2, temp2)
    plt.ylabel(r"Temperature$(K)$", size=14)
    plt.xlabel(r"1/capacitance$(pF^{-1})$", size=14)
    plt.plot(cdc2, lin(cdc2, *pov2), color="k", ls='-', label='Fit')
    plt.title(r"$1/C$ vs $T$ in decreasing $T$", size=16)
    text = "Slope= %0.3e +/- %0.3e\nIntercept= %0.3e +/- %0.3e" % (pov2[0], pocv2[0][0]**0.5, pov2[1], pocv2[1][1]**0.5)
    plt.text( 0.00090,405, text, size=10)
    plt.grid()
    plt.legend()
    plt.savefig("fit2.png")
    plt.show()
    plt.clf()


phase_trans()
para_ele()

