#Resolver Ecuaciones Diferenciales usando el Método de Runge-Kutta
from math import exp
import matplotlib.pyplot as mpl
def zeros(n): 
    z=n*[0]
    return z
def ecuaciondif(s,t): # La ecuacion diferencial que queremos resolver es= y'= t+(0.2*s*(t/N))-t
    return (0.2*s*(t))

#Esta función nos devuelve la solucion analítica, la cual usaremos para comparar los resultados del mètodo. 
def func(t): 
    return (4/1.3)*(exp(0.8*t)-exp(-0.5*t))+2*exp(-0.1*2*t)
    
    
T=list((i*4/50) for i in range(0,101))
#Queremos resolver la EDO en este rango con 100 fragmentos.

#Metodo de Runge-Kutta
W=zeros(101) # preasignacion.
t,h=2,4/100 # Y = y (0) establece el valor inicial y h = 4/50 es el tamaño.
W[0]=t
def RungeKutta4(t,Fun,h,s):
    #Estos son los coeficientes de Runge-Kutta de cuarto orden
    k1=Fun(s,t)
    k2=Fun(s+h/2,t+0.5*h*k1)
    k3=Fun(s+h/2,t+0.5*h*k2)
    k4=Fun(s+h,t+h*k3)
    phi=1/6*((k1)+2*(k2)+2*(k3)+(k4))*h
    return phi
    
  #Sustituyendo los coeficientes de orden 4 de Runge-Kutta tenemos:  
for i in range(len(T)-1):
    W[i+1]=t+RungeKutta4(t,ecuaciondif,h,T[i])
    t=W[i+1]
truevalue=list(func (i) for i in T)
  #Imprimo mis resultados.
print("El error máximo para el metodo de Runge-Kutta de cuarto orden es  ", max(list(abs(i-j) for i,j in zip(truevalue,W))))
print("Los puntos de la curva resultante para el método de Runge-Kutta son : ","\n")
for i,j in zip(T,W):
    print("t=",i,"=> y=",j)
#Imprimo la gráfica correspondiente.
ax=mpl.figure().add_subplot(1,1,1)
ax.plot(T,color="blue",label="Ajuste sin restricciones")
#ax.plot(W,color="red",label="Ajuste con restricciones")
ax.legend(loc=2)
mpl.show()