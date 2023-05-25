import numpy as np
import matplotlib.pyplot as plt

dt = 0.001
Tb = 1
t = np.arange(0,Tb,dt)
A = 1
fc = 100
wc = 2*np.pi*fc

sig = A*np.cos(wc*t)
mat_f = A*np.cos(2*np.pi*100*t)

m_out = np.sum(sig*mat_f*dt)
print(m_out)