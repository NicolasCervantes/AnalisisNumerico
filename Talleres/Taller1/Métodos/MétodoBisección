#Método de Bisección para encontrar las raices de una función dada

from matplotlib import pyplot
import numpy
import math

def f( x ):
    return math.e ** x - math.pi * x

def biseccion( a, b ):

    iteraciones = 0
    tolerancia = 10e-8
    c = ( a + b ) / 2
    errorX = []
    errorY = []
    
    if( f(a) * f(c) > 0 ):
        print("El intervalo no es apto para encontrar la raiz. ")
        

    while abs( b - a ) > tolerancia:
        
        c = ( a + b ) / 2
        funcionA = f( a )
        funcionC = f( c )
        
        if iteraciones > 0:
            errorX.append(abs( b - a ))
            
        iteraciones = iteraciones + 1
        
        if funcionC == 0:
            raiz = c
            break
     else if funcionA * funcionC < 0:
            b = c
        else:
            a = c
        raiz = c
        
        if iteraciones > 1:
            errorY.append(abs( b - a ))
        
    print("La aproximacion de la raiz de la funcion es: ", raiz )
    print("La cantidad de iteraciones obtenidas fueron ", iteraciones )

    x = numpy.linspace( errorX[0], errorX[len(errorX) - 1], 50 )
    y = numpy.linspace( errorY[0], errorY[len(errorY) - 1], 50 )
    pyplot.plot( x, y )
    pyplot.xlabel("Errores X ")
    pyplot.ylabel("Errores Y ")
    pyplot.title("Metodo de Biseccion: \n Error en X vs. Error en Y")
    pyplot.grid()
    pyplot.show()


if __name__ == "__main__":
    biseccion( 0, 1 )
    biseccion( 1, 2 )
