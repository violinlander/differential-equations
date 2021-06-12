import numpy as np
import matplotlib.pyplot as plt

#parameters

a = -10
b = 10

K = 1000

dx = (b - a) / K

x = np.linspace(a,b,K)
f = np.sin(x)

dfdx = np.zeros(f.shape[0]-2)

for i in range(len(dfdx)):
    dfdx[i] = (f[i+1] - f[i])/dx

fig, ax = plt.subplots(2)

ax[0].plot(x,f)
ax[1].plot(x[1:-1],dfdx)