import numpy as np

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

a = int(input("a: "))
K = int(input("K: "))
b = int(input("b: "))

df = ( b - a ) / K
x = [a + i*df for i in range(K)]


    