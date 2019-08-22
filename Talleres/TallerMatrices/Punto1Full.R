library(pracma)
library(matrix)

#Punto 1 Adicional Clase  
n = 6
rrr =sample(0:20, 36, replace = TRUE)
A = matrix( rrr, nrow=6, byrow=TRUE)
print(A)

cond = 0
while(cond< 1000 )
{
  A = matrix( sample(10:20, 36, replace = TRUE), nrow=n, byrow=TRUE)
  cond = condicional(A)
}
print("A")
print(A)

cond = (condicional(A))
print(cond)
b = matrix( c(1,2,3,4,5,6), nrow = 1, byrow=TRUE)
print("b")
print(b)

if(cond > 1000)
{
  print(cond)  
  diagonal <- function(M) 
  {
    M[col(M)!=row(M)] <- 0
    return(M)
  }
  
  
  #T = -D^-1(L + U)
  D = diagonal(A)
  L = tril(A,k=-1)
  U = triu(A,k=1)
  
  T = (-solve(D))%*%(L+U)
  print("Matriz de transición")
  print(T)
  print("Norma")
  norma <- norm(T,"F")
  print(norma)
  print("Radio espectral de la matriz")
  
  ev <- eig(A)
  abev <- abs(ev)
  radioExp <- max(abev)
  print( radioExp)
  
  
  # Matriz diagonal de dimension 3
  I=diag(1,nrow = nrow(A))
  # Matriz inversa de A
  D1 <- solve(D,I)
  T1 = D1 %*% U
  T2 = (I + (L %*% D1))
  # Matriz inversa de A
  T2<- solve(T2,I)
  
  #Análisis de convergencia
  MatTG = T1+T2
  normaG = norm(MatTG, type = c( "I"))
  print("Norma/convergencia de Gauss")
  print(normaG)
  print("Matriz de transición Gauss ")
  print(MatTG)
  
  MatTJ = (-D1)%*%(L+U)
  normaJ = norm(MatTJ, type = c("I"))
  print("Norma/convergencia de Jacobi")
  print(normaJ)
  print("Matriz de transición Jacobi")
  print(MatTJ)
  
  
}



# Punto 1 Taller. 
#Para el siguiente ejercicio, instale el paquete "pracma"

#-- a --
#Revise las siguientes funciones con la matriz del ejercicio 2


#Tamaño de la matriz
n = 4
A = matrix(c(2, 7, -6, 9,
             5, 1,8, 12,
             0, 6, 5, 8,
             3, 7, 1, 2), nrow=n, byrow=TRUE)
print("A")
print(A)

b = matrix(c(1.5,3,5,-4), nrow=n, byrow=TRUE)
print("b")
print(b)


D1 <- eye(n, m = n)
D2 <- ones(n, m = n)
D3 <- zeros(n, m = n)

print("D1")
D1
print("D2")
D2
print("D3")
D3

#El comando eye(n, m = n) permite obtener la matriz identidad de tamaño n, la cual está compuesta de ceros a excepción de la diagonal principal que contiene unos.
#El comando ones(n, m = n) permite obtener una matriz de tamaño n contenida únicamnete por unos.
#El comando zeros(n, m = n) permite obtener una matriz de tamaño n compuesta de ceros.



#-- b --
# b. Evalue la matriz de transicionn para el metodo SOR

U = A
L = A

#Aca se asignan las respectivas matrices diagonalizadas a cada variable
U[upper.tri(U, diag = TRUE)] <- 0
L[lower.tri(L,diag=TRUE)] <- 0
print (A)

#Obtienee la diagonal principal de la matriz
D1 = diag(diag(A^-1))

#Multiplicación de la matriz
T1 = D1 %*% U
I = D1
T2 = (I + (L %*% D1))
MatT = T1+T2
print(MatT)
