import numpy as np
import matplotlib.pyplot as plt

m=0
std=1
min=-20
max=20
dx=0.001
x=np.arange(min, max, dx)
g1=1/(np.sqrt(2*np.pi)*std)
g2=np.exp(-1*((x-m)**2)/(2*std**2))
gauss=g1*g2
p=np.sum(gauss*dx)
print(p)