#Implementación del método de Steffensen para encontrar las raices de una función dada
from matplotlib import pyplot
import numpy
import math

def f( x ):
    return math.e ** x - math.pi * x

def steffensen( x ):
    
    iteraciones = 0
    errorX = []
    errorY = []
    tolerancia = 10e-8
    
    while abs(f(x)) > tolerancia:
        
        if iteraciones > 0:
            errorX.append( abs(f(x)) )
        iteraciones = iteraciones + 1
        x = x - (f(x) ** 2 / (f(x + f(x)) - f(x)))
        if iteraciones > 1:
            errorY.append( abs(f(x)) )


    print("La raiz de la funcion es aproximadamente: ", x )
    print("La cantidad de iteraciones fueron: ", iteraciones )

    poli = numpy.polyfit(errorX, errorY, 2)
    poli2 = numpy.poly1d( poli )
    cdX = numpy.linspace( errorX[0], errorX[len(errorX) - 1], 50 )
    cdY = pol2( cdX )
    pyplot.plot( cdX, cdY )
    pyplot.xlabel("Errores X ")
    pyplot.ylabel("Errores Y ")
    pyplot.title("Metodo de Steffensen: \n Error en X vs. Error en Y")
    pyplot.grid()
    pyplot.show()


if __name__ == "__main__":
    steffensen( 1 )
    steffensen( 2 )
   
