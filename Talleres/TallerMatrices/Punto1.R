#Punto 1
library(pracma)
library(Matrix)

#Parte a
n=3
D1<-eye(n, m=n)#Diagonal de la matriz 
D2<-ones(n, m=n)#Llenar matriz de 1
D3<-zeros(n, m=n)#Llenar matriz de 0

#Matriz A
A = matrix(c(8, 9, 2,
             2, 7, 2,
             2, 8, 6), 
           nrow=n, byrow=TRUE)

#Matriz B
b = matrix(c(69,47,68), nrow=n, byrow=TRUE)

print(D1)
print(D2)
print(D3)

#Parte b
# w grado de relajación 0<w<2
fSOR<-function(a,n,w){
  D=a*eye(n, m=n)
  L<-a
  L[lower.tri(L, diag = FALSE)]<-0
  auxT=(D-(w*L))
  auxT1=inv(auxT)
  U<-a
  U[upper.tri(U, diag = FALSE)]<-0
  auxT2=((1-w)*D+(w*U))
  Tfinal=auxT1*auxT2
}
print(fSOR(A,3,1.5))

----------------------------------------------------------------------

#Segunda Matriz 

library(pracma)
library(Matrix)

#Parte a
n=6
c=6
D1<-eye(n, m=n)#Diagonal de la matriz 
D2<-ones(n, m=n)#Llenar matriz de 1
D3<-zeros(n, m=n)#Llenar matriz de 0

#Matriz A
A = matrix(c(sample(0:20), sample(0:20,1), sample(0:20,1), sample(0:20,1), sample(0:20,1), sample(0:20,1), 
             sample(0:20,1), sample(0:20,1), sample(0:20,1), sample(0:20,1), sample(0:20,1), sample(0:20,1),
             sample(0:20,1), sample(0:20,1), sample(0:20,1), sample(0:20,1), sample(0:20,1), sample(0:20,1),
             sample(0:20,1), sample(0:20,1), sample(0:20,1), sample(0:20,1), sample(0:20,1), sample(0:20,1),
             sample(0:20,1), sample(0:20,1), sample(0:20,1), sample(0:20,1), sample(0:20,1), sample(0:20,1),
             sample(0:20,1), sample(0:20,1), sample(0:20,1), sample(0:20,1), sample(0:20,1), sample(0:20,1)),
             nrow=n, ncol=c, byrow=TRUE)

print(A)

#Matriz B
b = matrix(c(1,2,3,4,5,6), nrow=n, byrow=TRUE)

print(D1)
print(D2)
print(D3)

#Parte b
# w grado de relajación 0<w<2
fSOR<-function(a,n,w){
  D=a*eye(n, m=n)
  L<-a
  L[lower.tri(L, diag = FALSE)]<-0
  auxT=(D-(w*L))
  auxT1=inv(auxT)
  U<-a
  U[upper.tri(U, diag = FALSE)]<-0
  auxT2=((1-w)*D+(w*U))
  Tfinal=auxT1*auxT2
}
print(fSOR(A,6,1.5))

