#Implementación del método Aitken para encontrar las raices de una función dada

from matplotlib import pyplot
import numpy
import math

def f( x ):
    return math.e ** x / math.pi

def aitken( x ):

    iteraciones = 0
    errorX = []
    errorY = []
    tolerancia = 10e-8
    x0 = x
    x1 = 0
    x2 = f( x0 )

    while abs(x2 - x1) > tolerancia:
        
        if iteraciones > 0:
            errorX.append(abs(x2 - x1))
        iteraciones = iteraciones + 1
        x0 = x2
        x2 = f(x0)
        x1 = x2
        x2 = f(x1)
        x0 = x2 - (((x2 - x1) ** 2) / (x2 - 2*(x1) + x0 ))
        x2 = f(x0)
        
        if iteraciones > 1:
            errorY.append(abs(x2 - x1))
    
    print("La raiz de la funcion aproximada es: ", x2 )
    print("La cantidad de iteraciones fueron: ", iteraciones )

    poli = numpy.polyfit(errorX, errorY, 2)
    poli2 = numpy.poly1d( poli )
    cdX = numpy.linspace( errorX[0], errorX[len(errorX) - 1], 50 )
    cdY = pol2( cdX )
    pyplot.plot( cdX, cdY )
    pyplot.xlabel("Errores X ")
    pyplot.ylabel("Errores Y ")
    pyplot.title("Metodo de Aitken: \n Error en X vs. Error en Y")
    pyplot.grid()
    pyplot.show()
        

if __name__ == "__main__":
    aitken( 1 )
