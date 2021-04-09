import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from scipy.optimize import curve_fit

lin=lambda x,a,b : a +x*b
def an1():
    df = pd.read_excel(r'c:\Users\prita\Desktop\python_project\lab_solid_state\magneto_resistance\mag.xlsx', sheet_name='bismuth')
    no='140'
    H = df['H_'+no].tolist()
    dr = df['DR/R_'+no].tolist()

    logH = df['logH_'+no].tolist()[1:]
    logdr = df['logdr_'+no].tolist()[1:]
    fig,ax=plt.subplots(1,2)

    ax[0].plot(H,dr,'ro',label= 'Data points')
    ax[0].legend()
    ax[0].set_xlabel("H (in G)")
    ax[0].set_ylabel(r"$ \frac{\Delta R }{ R} $",size=16)
    ax[0].grid()
    logH=np.array(logH)    
    pov,pocv = curve_fit(lin,logH,logdr)
    ax[1].plot(logH,logdr,'ro',label= 'Data points')
    ax[1].plot(logH,lin(logH,*pov),label="Fit")
    ax[1].legend()
    ax[1].set_xlabel("logH")
    ax[1].set_ylabel(r"$log \frac{\Delta R }{ R} $",size=16)
    ax[1].grid()
    ax[1].text(3.2,-1.6,"Slope = {1} +/- {3}\n Intercept = {0} +/- {2}".format(*np.round(pov,3),*np.round(np.sqrt(np.diag(pocv)),3)))
    plt.show()

def an2():
    df = pd.read_excel(r'c:\Users\prita\Desktop\python_project\lab_solid_state\magneto_resistance\mag.xlsx', sheet_name='bismuth')
    no='185'
    H = df['H_'+no].tolist()
    dr = df['DR/R_'+no].tolist()

    logH = df['logH_'+no].tolist()[1:]
    logdr = df['logdr_'+no].tolist()[1:]
    fig,ax=plt.subplots(1,2)
    ax[0].plot(H,dr,'ro',label= 'Data points')
    ax[0].legend()
    ax[0].set_xlabel("H (in G)")
    ax[0].set_ylabel(r"$ \frac{\Delta R }{ R} $",size=16)
    ax[0].grid()
    logH=np.array(logH)
    pov,pocv = curve_fit(lin,logH,logdr)
    ax[1].plot(logH,logdr,'ro',label= 'Data points')
    ax[1].plot(logH,lin(logH,*pov),label="Fit")
    ax[1].legend()
    ax[1].set_xlabel("logH")
    ax[1].set_ylabel(r"$log \frac{\Delta R }{ R} $",size=16)
    ax[1].grid()
    ax[1].text(3.2,-1.6,"Slope = {1} +/- {3}\n Intercept = {0} +/- {2}".format(*np.round(pov,3),*np.round(np.sqrt(np.diag(pocv)),3)))
    plt.show()

def an3():
    df = pd.read_excel(r'c:\Users\prita\Desktop\python_project\lab_solid_state\magneto_resistance\mag.xlsx', sheet_name='nGe')
    no='4.65'
    H = df['H_'+no].tolist()
    dr = df['DR/R_'+no].tolist()

    logH = df['logH_'+no].tolist()[1:]
    logdr = df['logdr_'+no].tolist()[1:]
    fig,ax=plt.subplots(1,2)
    ax[0].plot(H,dr,'ro',label= 'Data points')
    ax[0].legend()
    ax[0].set_xlabel("H (in G)")
    ax[0].set_ylabel(r"$ \frac{\Delta R }{ R} $",size=16)
    ax[0].grid()
    logH=np.array(logH)
    pov,pocv = curve_fit(lin,logH,logdr)
    ax[1].plot(logH,logdr,'ro',label= 'Data points')
    ax[1].plot(logH,lin(logH,*pov),label="Fit")
    ax[1].legend()
    ax[1].set_xlabel("logH")
    ax[1].set_ylabel(r"$log \frac{\Delta R }{ R} $",size=16)
    ax[1].grid()
    ax[1].text(3.2,-2.6,"Slope = {1} +/- {3}\n Intercept = {0} +/- {2}".format(*np.round(pov,3),*np.round(np.sqrt(np.diag(pocv)),3)))
    plt.show()

def an4():
    df = pd.read_excel(r'c:\Users\prita\Desktop\python_project\lab_solid_state\magneto_resistance\mag.xlsx', sheet_name='nGe')
    no='7.26'
    H = df['H_'+no].tolist()
    dr = df['DR/R_'+no].tolist()

    logH = df['logH_'+no].tolist()[1:]
    logdr = df['logdr_'+no].tolist()[1:]
    fig,ax=plt.subplots(1,2)
    ax[0].plot(H,dr,'ro',label= 'Data points')
    ax[0].legend()
    ax[0].set_xlabel("H (in G)")
    ax[0].set_ylabel(r"$ \frac{\Delta R }{ R} $",size=16)
    ax[0].grid()
    logH=np.array(logH)
    pov,pocv = curve_fit(lin,logH,logdr)
    ax[1].plot(logH,logdr,'ro',label= 'Data points')
    ax[1].plot(logH,lin(logH,*pov),label="Fit")
    ax[1].legend()
    ax[1].set_xlabel("logH")
    ax[1].set_ylabel(r"$log \frac{\Delta R }{ R} $",size=16)
    ax[1].grid()
    ax[1].text(3.2,-2.6,"Slope = {1} +/- {3}\n Intercept = {0} +/- {2}".format(*np.round(pov,3),*np.round(np.sqrt(np.diag(pocv)),3)))
    plt.show()


an1()