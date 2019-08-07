#Método de Punto Fijo para encontrar las raices de una función dada

from matplotlib import pyplot
import numpy
import math

def G1( x ):
    return math.e ** x / math.pi

def G2( x ):
    return math.log( math.pi * x )

def pFijo1( a, b ):

    x = ( a + b) / 2
    tolerancia = 10e-8
    iteraciones = 0
    errorX = []
    errorY = []
    
    while abs(G1(x) - x) > tolerancia :
        if iteraciones > 0:
            errorX.append( abs(G1(x) - x) )
        iteraciones = iteraciones + 1
        x = G1(x)
        if iteraciones > 1:
            errorY.append( abs(G1(x) - x) )

    print("La raiz encontrada en el intervalo ", a, ", ", b, " con la funcion g(x) = e ^ x / PI es aproximadamente: ", x )
    print("El numero de iteraciones fueron: ", iteraciones )

    cdX = numpy.linspace( errorX[0], errorX[len(errorX) - 1], 50 )
    cdY = numpy.linspace( errorY[0], errorY[len(errorY) - 1], 50 )
    pyplot.plot(cdX, cdY)
    pyplot.xlabel("Errores X ")
    pyplot.ylabel("Errores Y ")
    pyplot.title("Metodo de Punto Fijo: \n Error en X vs. Error en Y")
    pyplot.grid()
    pyplot.show()

def pFijo2( a, b ):
    
    x = ( a + b) / 2
    iteraciones = 0
    tolerancia = 10e-8
    errorX = []
    errorY = []
    
    while abs(G2(x) - x) > tolerancia:
        if iteraciones > 0:
            errorX.append( abs(G2(x) - x))
        x = G2(x)
        if iteraciones > 1:
            errorY.append( abs(G2(x) - x)) 
        iteraciones = iteraciones + 1
    
    print("La raiz encontrada en el intervalo ", a, ", ", b, " con la funcion g(x) = ln( PI * x ) es aproximadamente: ", x )
    print("El numero de iteraciones fueron: ", iteraciones )

    cdX = numpy.linspace( errorX[0], errorX[len(errorX) - 1], 50 )
    cdY = numpy.linspace( errorY[0], errorY[len(errorY) - 1], 50 )
    pyplot.plot(cdX, cdY)
    pyplot.xlabel("Errores X ")
    pyplot.ylabel("Errores Y ")
    pyplot.title("Metodo de Punto Fijo: \n Error en X vs. Error en Y")
    pyplot.grid()
    pyplot.show()


if __name__ == "__main__":
    pFijo1( 0, 1 )
    pFijo2( 1, 2 )
