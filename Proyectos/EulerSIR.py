import numpy as np
from matplotlib import pyplot as plt

xi = 0
yi = 0
xf = 30
n = 100
h = (xf - xi) / (n)
N = 20

t = np.linspace(xi, xf, n)
y = np.zeros([n])
b = 0.2
r = 0.3
s = np.linspace(xi,xf,n) 
y[0] = yi	

for i in range (1, n ):
    y[i]= t[i] + b*s[i]*(t[i]/N) - r*t[i]


for i in range(n):
    print(y[i])


plt.plot(y, 'o')
#plt.xlabel("Valor de x")
plt.ylabel("Valor de y")
plt.title("Solución con método de Euler")
plt.show( ) 

