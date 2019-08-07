#Algoritmo que calcula aproximadamente la raiz cuadrada de un número n 

def calcRaiz( n ):
    x = 0.1
    Tolerancia = 10e-8
    y = (1/2) * (x + (n/x))
    while abs(x - y) > Tolerancia:
        x = y
        y = (1/2) * (x + (n/x)) 
    print("La raiz cuadrada aproximada del numero ", n, "es: ", y)

if __name__ == "__main__":
    calcRaiz( 7 )
