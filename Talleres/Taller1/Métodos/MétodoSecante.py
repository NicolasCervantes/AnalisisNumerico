#Implementación del método de Secante para encontrar las raices de una función dada
from matplotlib import pyplot
import numpy
import math

def f( x ):
    return math.e ** x - math.pi * x

def secante( x0, x1 ):
    
    iteraciones = 0
    tolerancia = 10e-8
    errorX = []
    errorY = []
    f0 = f( x0 )
    f1 = f( x1 )
    
    while abs(x1 - x0) > tolerancia:
        
        if iteraciones > 0:
            errorX.append( abs(x1 - x0) )
        iteraciones = iteraciones + 1
        m = (f1 - f0 )/(x1 - x0)
        if m == 0:
            break
        x2 = x1 - f1 / m
        f2 = f( x2 )
        x0 = x1
        x1 = x2
        f0 = f1
        f1 = f2
        
        if iteraciones > 1:
            errorY.append( abs(x1 - x0) )
   

    print("La raiz de la funcion es aproximadamente: ", x2 )
    print("La cantidad de iteraciones fueron: ", iteraciones )

    poli = numpy.polyfit(errorX, errorY, 2)
    poli2 = numpy.poly1d( poli )
    cdX = numpy.linspace( errorX[0], errorX[len(errorX) - 1], 50 )
    cdY = poli2( cdX )
    pyplot.plot( cdX, cdY )
    pyplot.xlabel("Errores X ")
    pyplot.ylabel("Errores Y ")
    pyplot.title("Metodo de Secante: \n Error en X vs. Error en Y")
    pyplot.grid()
    pyplot.show()


if __name__ == "__main__":
    secante( 0, 1 )
    secante( 1, 2 )
