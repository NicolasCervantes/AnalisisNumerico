rm(list=ls())

library(pracma)
library(Matrix)

#Punto 2 Adicional ----------------------

# Matrices necesarias
n = 3
A = matrix(c(8,9,2,
             2,7,2,
             2,8,5), nrow=n, byrow=TRUE)
print(A)

b = matrix(c(69,47,88), nrow=3, byrow=TRUE)
print(b)



U = A
L = A
L[lower.tri(L,diag=TRUE)] <- 0
U[upper.tri(U, diag = TRUE)] <- 0


D = diag(diag(A))
# Matriz diagonal de dimension 3
I=diag(1,nrow = nrow(A))
# Matriz inversa de A
D1 <- solve(D,I)
T1 = D1 %*% U
T2 = (I + (L %*% D1))
# Matriz inversa de A
T2<- solve(T2,I)

MatTG = T1+T2
normaG = norm(MatTG, type = c( "I"))
print("Norma de Gauss")
print(normaG)
print("Matriz de transición Gauss")
print(MatTG)

MatTJ = (-D1)%*%(L+U)
normaJ = norm(MatTJ, type = c("I"))
print("Norma de Jacobi")
print(normaJ)
print("Matriz de transición Jacobi")
print(MatTJ)


#Punto 2 Taller -------------------------------
n=4#Tam matriz
#Matriz A
A = matrix(c(-8.1, -7, 6.123, -2,
             -1, 4,-3, -1,
             0, -1, -5, 0.6,
             -1, 0.33, 6, 1/2), 
           nrow=n, byrow=TRUE)
#Matriz B
b = matrix(c(1.45,3,5.12,-4), nrow=n, byrow=TRUE)

toleracia=1e-9

#Punto A
#descomposicion

jacobi<-function(a,n){
  D=a*eye(n, m = n)
  L<-a
  L[lower.tri(L, diag = FALSE)]<-0
  U<-a
  U[upper.tri(U, diag = FALSE)]<-0
  AA=D+L+U
  print(AA)
}
jacobi(A,4)

#Punto b
solGS=itersolve(A,b,x0=c(1,2,1,1),toleracia,method = "Gauss-Seidel")
print(solGS)

#Punto c
solJacobi=itersolve(A, b, x0 = c(1,2,1,1), nmax = 5, toleracia, method = c("Jacobi"))
print(solJacobi)
