import numpy as np
import matplotlib.pyplot as plt

s0 = 0
sf = 30
b = 0.2
r = 0.3
t0 = 0
n = 100
h = (sf-s0)/n
s = np.linspace(s0,sf+h,h)
t= np.zeros(n)
t[0] = t0

def f(s,t):
	for i in range(0,n):
		return t[i] + b*s[i]*(t[i]/N) - r*t[i]

def rk4(f,s0,sf,t0,h):
	for i in range(0,n-1):
		k1 = f(s[i],t[i])
		k2 = f(s[i]+h/2, t[i]+k1*h/2)
		k3 = f(s[i]+h/2, t[i]+k2*h/2)
		k4 = f(s[i]+h, t[i]+k3*h)
		t[i+1] = t[i]+(h/6)*(k1+2*k2+2*k3+k4)
	plt.plot(s,t)	
	plt.show()
