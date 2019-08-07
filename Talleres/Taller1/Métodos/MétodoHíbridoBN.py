#Método Hibrido (Biseccion-Newton) para encontrar las raices de una función dada
import matplotlib
from matplotlib import pyplot
import numpy
import math

def f( x ):
    return math.e ** x - math.pi * x

def fd( x ):
    return math.e ** x - math.pi

def hibrido( a, b ):
    
    iteraciones = 0
    tolerancia = 10e-8
    errorX = []
    errorY = []
    c = (a + b) / 2
    
    if c - f(c) / fd(c) > a and c - f(c) / fd(c) < b:
        x = c - f(c) / fd(c)
    else:
        x = (a + b) / 2
    
    while abs(f(x)) > tolerancia:
        
        if iteraciones > 0:
            errorX.append( abs(f(x)) )
        iteraciones = iteraciones + 1
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        
        c = (a + b) / 2
        if c - f(c) / fd(c) > a and c - f(c) / fd(c) < b:
            x = c - f(c) / fd(c)
        else:
            x = (a + b) / 2
        
        if it > 1:
            errorY.append( abs(f(x)) )

    
    print("La raiz de la funcion aproximada es: ", x )
    print("La cantidad de iteraciones fueron: ", iteraciones )

    poli = numpy.polyfit(errorX, errorY, 2)
    poli2 = numpy.poly1d( poli )
    cdX = numpy.linspace( errorX[0], errorX[len(errorX) - 1], 50 )
    cdY = pol2( cdX )
    pyplot.plot( cdX, cdY )
    pyplot.xlabel("Errores X ")
    pyplot.ylabel("Errores Y ")
    pyplot.title("Metodo Hibrido Newton-Biseccion: \n Error en X vs. Error en Y")
    pyplot.grid()
    pyplot.show()

    cdY = numpy.linspace( errorY[0], errorY[len(errorY) - 1], 50 )
    matplotlib.pyplot.plot(cdX, cdY)
    matplotlib.pyplot.xlabel("Errores X ")
    matplotlib.pyplot.ylabel("Errores Y ")
    matplotlib.pyplot.title("Metodo Hibrido Newton-Biseccion: \n Errores en X vs. Errores en Y")
    matplotlib.pyplot.grid()
    matplotlib.pyplot.show()


if __name__ == "__main__":
    hibrido( 0, 1 )
    hibrido( 1, 2 )
