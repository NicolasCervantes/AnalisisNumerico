library(pracma)
# Prueba
A = matrix(c(  3.5,  4.2,  
               1/2,   1/3  
), nrow=2, byrow=TRUE)
k = 5
#se acaba la prueba 
mp <- A 


#Obtiene valores propios para hacer D
valoresPropios <- eigen(mp)$values
#Obtiene vectores propios para hacer P
vectoresPropios <-  eigen(mp)$vectors
#longitud de nuevas matrices
valoresPropiosTam <- length(valoresPropios)
vectoresPropiosTam <- valoresPropiosTam
#creacion de D, que es la diagonal
D <- Diag(valoresPropios)
#creacion de P, que son los vectores propios
P <-matrix(vectoresPropios, vectoresPropiosTam, vectoresPropiosTam)
#creacion de inverso P, con error si la matriz no tiene 
pInverso <- tryCatch({
  solve(P)
}, error = function(e){print("La matriz no tiene inverso")})

#Mostrar los parametros
print("La matriz A definida por ")
mp
print("Tiene la diagonal D: ")
D

print("Una Matriz de vectores propios P de: ")
P

print("Y el inverso de P es: ")
pInverso
print("Y la multiplicacion de P*D*Pinverso es")
P %*% D %*% pInverso
print("Y esto equivale a A")
#for loop para multiplicar D
dim = seq(0,k,1)
for(val in dim){
  D = D %*% D
}
cat("Y D a un número k, donde k = ", k, " es igual a")
D
cat("Finalmente (P)(D)^k(Pinverso) es igual a A^k, y eso se representa en la matriz: ")
P %*% D %*% pInverso
