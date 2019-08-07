#Método que permite evaluar un polinomio 2X⁴-3X²+3X-4 (donde X = -2) con el número minimo de multiplicaciones y sumas  

def horner( x ):
    
    coeficiente = [2, 0, -3, 3, -4]
    resultado = 0
    
    for i in range(len(coef)):
        resultado = resultado * x + coeficiente[i]
    
    print("El resultado del polinomio evaluado en X= ", x, " es igual a: ", resultado)

if __name__ == "__main__":
    horner( -2 )
