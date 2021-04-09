import matplotlib.pylab as plt
import numpy as np
# from scipy.optimize import curve_fit
from pandas import read_excel


def sun():
    lengths = ['0', 'pink', 'blue', 'green', 'red', 'yellow']
    for sh in lengths:
        unit = '$m$'
        df = read_excel("sun.xlsx", sheet_name = 's_%s'%sh)
        df.dropna()
        i = np.array(df['I'].tolist())
        v = np.array(df['V'].tolist())
        p = np.array(df['p'].tolist())
        m_v = v[0]
        m_p = p.max()
        m_i = i[-1]
        text = r"$P_{max}$ = "+f'{m_p}'+'%sW\n'%unit+r"$I_{sc}$ = "+f'{m_i}'+'%sA\n'%unit+r'$V_{oc}$ = '+f'{m_v}V'
        plt.text(m_v/3.1, m_i/5, text, fontsize="12")
        plt.plot(v, i, c='black', ls='-', marker='o', label='data points', lw="1.8", markersize="9", markerfacecolor="red")
        plt.xlabel(r"V$(Volt)$",fontsize=14)
        plt.ylabel(r"I$(%sA)$" % unit, fontsize=14)
        if sh == '0':
            plt.title("No filter",fontsize = 16)
        else: plt.title("Filter color = %s"%sh, fontsize= 16)
        plt.legend(loc="lower center")
        plt.grid()
        plt.savefig("IV_%s.png" % sh, dpi=600)
        plt.show()

        plt.plot(v, p, c='black',ls='-',marker ='^',label='data', lw='1.8', markersize="10", markerfacecolor="blue")
        text = r"$P_{max}$ = "+f'{m_p}'+'%sW\n'% unit
        plt.xlabel(r"V$(Volt)$",fontsize=14)
        plt.ylabel("P(%sW)"%unit, fontsize=14)
        plt.text(m_v/3.1, m_i/5, text, fontsize="12")
        if sh == '0':
            plt.title("No filter", fontsize = 16)
        else: plt.title("Filter color = %s"%sh, fontsize= 16)
        plt.legend(loc='upper center')
        plt.grid()
        plt.savefig("PV_%s.png" % sh, dpi=600)
        plt.show()


def moon():
    lengths = [0, 460, 500, 540, 570, 635]
    for sh in lengths:
        unit = '$\mu$' if sh == 460 or sh == 500 else 'm'
        df = read_excel("moon.xlsx", sheet_name='m_%d' % sh)
        df.dropna()
        i = np.array(df['I'].tolist())
        v = np.array(df['V'].tolist())
        p = np.array(df['p'].tolist())
        m_v = v[0]
        m_p = p.max()
        m_i = i[-1]
        text = r"$P_{max}$ = "+f'{m_p}'+'%sW\n'%unit+r"$I_{sc}$ = "+f'{m_i}'+'%sA\n'%unit+r'$V_{oc}$ = '+f'{m_v}V'
        plt.text(m_v/3.1, m_i/5, text, fontsize=12)
        plt.plot(v, i, c='black', ls='-', marker='s', label='data points', lw="1.8", markersize="8", markerfacecolor="red")
        plt.xlabel(r"V$(Volt)$", fontsize=14)
        plt.ylabel("I(%sA)" % unit, fontsize=14)
        if sh == 0:
            plt.title("No filter", fontsize=16)
        else: plt.title("Wavelength of filter =%d nm" % sh, fontsize=16)
        plt.legend(loc="lower center")
        plt.grid()
        plt.savefig("IVm_%s.png" % sh, dpi=600)
        plt.show()

        text = r"$P_{max}$ = " + f'{m_p}' + '%sW\n' % unit
        plt.plot(v, p, c='black', ls='-', marker='v', label='data points', lw='1.8', markersize="10", markerfacecolor="blue")
        plt.xlabel(r"V$(Volt)$", fontsize=14)
        plt.ylabel("P(%sW)" % unit, fontsize=12 )
        plt.text(m_v / 3, m_i / 7.5, text, fontsize=12)
        plt.legend(loc='best')
        if sh == 0:
            plt.title("No filter",fontsize=16)
        else: plt.title("Wavelength of filter =%d nm" % sh, fontsize=16)
        plt.grid()
        plt.savefig("PVm_%s.png" % sh, dpi=600)
        plt.show()


sun()
moon()
