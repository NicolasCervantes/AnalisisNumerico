#Algoritmo que aproxima el resultado de un polinomio usando el teorema de taylor para la función f(x)=e^0.5

import math

def aproxTaylor():
    
    resulReal = math.e ** 0.5
    resulAprox = 0.0
    grado = int(input("Digite el grado del polinomio de Taylor. "))
    x = 0
    
    for i in range(grado):
        resulAprox = resulAprox + (((math.e ** x) * (0.5 ** i)) / math.factorial(i))
        
    print("El resultado real es: ", round(resulReal, 4))
    print("El resultado aproximado es: ", round(resulAprox, 4))

if __name__ == "__main__":
    aproxTaylor()
