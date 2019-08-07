#Método de Posición Falsa para encontrar las raices de una función dada
from matplotlib import pyplot
import numpy
import math

def f( x ):
    return math.e ** x - math.pi * x

def posicionF( a, b ):
    
    iteraciones = 0
    tolerancia = 10e-8
    errorX = []
    errorY = []
    maxIteraciones = 7
    
    rf = (a * f(b) - b * f(a)) / (f(b) - f(a) )
    errorA = rf - a
    errorB = b - rf
    
    while max(errorA, errorB ) > tolerancia and iteraciones < maxIteraciones:
        
        if iteraciones > 0:
            errorX.append( max(abs(errorA), abs(errorB)) )
        iteraciones = iteraciones + 1
        if f(rf) * f(a) > 0:
            a = rf
        else:
            b = rf
        
        rf = (a * f(b) - b * f(a)) / (f(b) - f(a) )
        errorA = rf - a
        errorB = b - rf
        
        if iteraciones > 1:
            errorY.append( max(abs(errorA), abs(errorB)) )
        
    print("La raiz de la funcion es aproximadamente:  ", rf )
    print("La cantidad de iteraciones fueron: ", iteraciones )

    cdX = numpy.linspace( errorX[0], errorX[len(errorX) - 1], 50 )
    cdY = numpy.linspace( errorY[0], errorY[len(errorY) - 1], 50 )
    pyplot.plot( cdX, cdY )
    pyplot.xlabel("Errores X ")
    pyplot.ylabel("Errores Y ")
    pyplot.title("Metodo de Posicion Falsa: \n Error en X vs. Error en Y")
    pyplot.grid()
    pyplot.show()
    

if __name__ == "__main__":
    posicionF( 0, 1 )
    posicionF( 1, 2 )
