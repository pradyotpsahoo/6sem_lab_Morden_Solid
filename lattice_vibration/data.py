import numpy as np
import matplotlib.pylab as plt
L = 1.0342e-3
C = 57.98e-9
C1 = 0.1728e-6


def f():
    a="%0.5e"%(1/np.pi/(L*C)**0.5)
    print(a)

def m_theta(f):
    f=float(f)
    f=f*1e3
    a = '%3.3f'%(np.arccos(1-2*f**2*np.pi**2*L*C)*180/np.pi)
    print(a)

def fdi(t):
    
    p=1/C + 1/C1
    q= C*C1
    f1 = (p/L + (p**2 -4*np.sin(t*np.pi/180)**2/q)**0.5/L)**0.5/2/np.pi
    f2 = (p/L - (p**2 -4*np.sin(t*np.pi/180)**2/q)**0.5/L)**0.5/2/np.pi
    #f2 = p/L + (p**2 -4*np.sin(t*np.pi/180)**2/q)**0.5/L

    #print('%0.6e'%f1)
    #print('%0.6e'%f2)
    return [f1,f2]


t=np.linspace(0,180,500)
plt.plot(t,fdi(t)[0]/1e3)
plt.plot(t,fdi(t)[1]/1e3)
plt.show()

