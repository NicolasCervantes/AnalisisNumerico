#Resolver una función producto de una integral 
import math
from matplotlib import pyplot
import numpy

def f( x ):
    return - math.e ** x + 5 * x - 1

def g( x ):
    return (math.e ** x + 1 ) / 5

def pFijo( a, b ):
    
    iteraciones = 0
    itMaximas = 5
    tolerancia = 10e-8
    error = []
    x = (a + b) / 2
    
    while abs(g(x) - x) > tolerancia and iteraciones < itMaximas:
        error.append( abs(g(x) - x) )
        x = g(x)
        iteraciones = iteraciones + 1
    
    print("La raiz que está en el intervalo ", a, ", ", b, "es aproximadamente: ", x )
    print("El numero de iteraciones fueron: ", iteraciones )
    
    cdX = numpy.linspace( 1, iteraciones, 50 )
    y = numpy.linspace( error[0], error[len(error) - 1], 50)
    pyplot.plot(cdX, y )
    pyplot.xlabel("Iteraciones")
    pyplot.ylabel("Error")
    pyplot.grid()
    pyplot.show()

if __name__ == "__main__":
    pFijo( 0, 1 )
