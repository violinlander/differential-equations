
import numpy as np
import matplotlib.pyplot as plt

import sys

# Print some introduction and instruction:

print("This script was created using Python 3 " + '3.7.3 (default, Jan 22 2021, 20:04:44) \n[GCC 8.3.0]')
print("Your version is {}".format(sys.version))
print("\n\n")


print("Here's how this is going to work. The domain of definition will")
print("discretized according to this diagram: \n")
with open("1DGridDiagram.txt","r") as f:
    print(f.read())
print()


# Input parameters

a = -3.3 #int(input("a: "))
K = 10000 #int(input("K: "))
b = 0 #int(input("b: "))

dx = (b-a)/K

df = ( b - a ) / K
x = np.linspace(a,b,K)


# Poisson EQ: d2f/dx^2 + g = 0

# g is zero for all x_i
def gg(a):
    return a**3+5*a**2+7*a + 2

g = [gg(a) for a in x]

fig = plt.figure()
fig
axes = fig.add_axes([a,0,dx,1])
fig.show()

    