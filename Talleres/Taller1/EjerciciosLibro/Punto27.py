#Encontrar en que momento dos coordenadas son iguales en el intervalo de 0 a pi/2

from matplotlib import pyplot
import numpy

def x( t ):
    return 3 * numpy.sin(t)**3 - 1

def y( t ):
    return 4 * numpy.sin(t) * numpy.cos(t)

def h( t ):
    return (3 * numpy.sin(t)**3 - 1) - (4 * numpy.sin(t) * numpy.cos(t))

def interseccion( a, b ):
    
    c = (a + b) / 2
    iteraciones = 0
    error = []
    tolerancia = 10e-5
    
    
    while abs( b - a ) > tolerancia:
        
        c = ( a + b ) / 2
        funcionA = h( a )
        funcionC = h( c )
        error.append(abs( b - a ))
        if funcionC == 0:
            raiz = c
            break
        elif funcionA * funcionC < 0:
            b = c
        else:
            a = c
        raiz = c
        
        iteraciones = iteraciones + 1
        
    print("La raiz aproximada de la funcion es: ", raiz )
    print("La cantidad de iteraciones fueron: ", iteraciones )
    
    t = numpy.linspace( 0, numpy.pi/2, 1000 )
    fig = pyplot.figure()
    f = fig.add_subplot(111, projection="polar")
    g = fig.add_subplot(111, projection="polar")
    z = fig.add_subplot(111, projection="polar")
    f.plot(t, x(t), label='Funcion F' )
    g.plot(t, y(t), label='Funcion G' )
    z.plot(t, h(t), label='Funcion H' )
    pyplot.legend(prop = {'size':10}, loc = 'lower right')
    pyplot.show()
    
if __name__ == "__main__":
    interseccion( 0, numpy.pi/2 )
