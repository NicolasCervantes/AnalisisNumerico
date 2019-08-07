#Método de Newton para encontrar las raices de una función dada
from matplotlib import pyplot
import numpy
import math

def f( x ):
    return math.e ** x - math.pi * x

def fd( x ):
    return math.e ** x - math.pi

def newton( a, b ):

    x = (a + b) / 2
    iteraciones = 0
    tolerancia = 10e-8
    errorX = []
    errorY = []
    
    raiz = x - ( f(x) / fd(x) ) 

    while abs( raiz - x ) > tolerancia:
        if iteraciones > 0:
            errorX.append( abs( raiz - x ) )
        iteraciones = iteraciones + 1
        x = raiz
        raiz = x - ( f(x) / fd(x) ) 
        if iteraciones > 1:
            errorY.append( abs( raiz - x ) )
    
    print("La raiz encontrada en el intervalo ", a, ", ", b, " es aproximadamente: ", raiz )
    print("El numero de iteraciones fueron: ", iteraciones )
    
    poli = numpy.polyfit(errorX, errorY, 2)
    poli2 = numpy.poly1d( poli )
    cdX = numpy.linspace( errorX[0], errorX[len(errorX) - 1], 50 )
    cdY = pol2( cdX )
    pyplot.plot( cdX, cdY )
    pyplot.xlabel("Errores X ")
    pyplot.ylabel("Errores Y ")
    pyplot.title("Metodo de Newton: \n Error en X vs. Error en Y")
    pyplot.grid()
    pyplot.show()
    

if __name__ == "__main__":
    newton( 0, 1 )
    newton( 1, 2 )
