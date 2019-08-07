#Algoritmo que calcula aproximadamente la raíz n-ésima de un número

def raizNEsima( n, Num, vi ):
    
    tolerancia = 10e-8
    iteraciones = 0
    vir = 1
    
    while abs(vir) > tolerancia:
        
        iteraciones = iteraciones + 1
        vir = ((Num / (vi ** (n - 1))) - vi ) / n
        vi = vi + vir

    print("La raiz", n, "-esima de ", Num, "es aproximadamente", vi)
    print("Se tuvieron:", it, " iteraciones. ")


if __name__ == "__main__":
    Num = float(input("Digite un numero. "))
    n = float(input("Digite el valor de la raiz a calcular. "))
    vi = float(input("Digite un valor inicial. "))
    raizNEsima( n, Num, vi )
