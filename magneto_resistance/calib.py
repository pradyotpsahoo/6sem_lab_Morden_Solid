import pandas
import matplotlib.pyplot as plt

file2 = "C://Users/prita/Desktop/python_project/lab_solid_state/magneto_resistance/magneto_resistance.xlsx"


def cali():
    df = pandas.read_excel(file2, sheet_name="calib")
    print(df)
    curr = df['current(A)'].tolist()
    h1 = df['B(10*g)1'].tolist()
    h2 = df['B(10*g)2'].tolist()

    plt.plot(curr, h1, "go", ls='-', label="Data", markersize="10", linewidth="1")
    plt.legend(shadow=True, ncol=2, loc="best").set_draggable(True)
    plt.xlabel(r"$Current(A)$", size="14")
    plt.ylabel(r"Magnetic field $(10\times Gauss)$",size="14")
    plt.title(r"For calibration of $B$ for $(3Am.-0Am.)$", size="14")
    plt.grid()
    plt.show()

    plt.plot(curr, h2, "go", ls='-', label="Data", markersize="10", linewidth="1")
    plt.legend(shadow=True, ncol=2, loc="best").set_draggable(True)
    plt.xlabel(r"$Current(A)$", size="14")
    plt.ylabel(r"Magnetic field $(10\times Gauss)$",size="14")
    plt.title(r"For calibration of $B$ for $(0Am.-3Am.)$", size="14")
    plt.grid()
    plt.show()


cali()