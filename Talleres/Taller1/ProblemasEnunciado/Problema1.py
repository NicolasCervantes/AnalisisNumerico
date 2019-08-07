#Algoritmo que calcula el error de redondeo de un número
import math

def truncarNumero( N, decimal ):
    return math.floor( N * 10 ** decimal ) / 10 ** decimal

def errorN( N, decimal ):
    
    iteraciones = 0
    NumReal = N
    NM = 3 - decimal
    
    while NumReal > 1:
        NumReal = NumReal / 10
        iteraciones = iteraciones + 1
    
    NumAprox = truncarNumero( NumReal, decimal )
    error = (NumReal - NumAprox) * 10 ** 3
    
    print("El error de redondeo es :", round(error, 2), "* 10 ^", NM )  
  
if __name__ == "__main__":
    errorN( 536.78, 4 )
