#Punto A

rm(list=ls())
alpha <- 5
beta  <- 4
B = matrix(c(   2   ,0,-1   ,                                                                                
                beta,2,-1   ,                                                                         
                -1  ,1,alpha), nrow=3, byrow= TRUE)
b <- c(1,2,1)
solve(B,b)


#Punto B

rm(list=ls())
alpha <- 5
beta  <- 3
B = matrix(c(   2   ,0,-1   ,                                                                                
                beta,2,-1   ,                                                                         
                -1  ,1,alpha), nrow=3, byrow= TRUE)
b <- c(1,2,3)
resp <- solve(B,b)
for( i in c(1:9))
{
  resp <- solve(B,resp)
  print(resp)
}


#Punto C

rm(list=ls())
jacobi<-function(a,ciclos) 
{
  n<-nrow(a)
  id <- matrix(0, n, n)
  diag(id) <- 1
  Q<-id
  for (k in 1:ciclos) {
    for ( i in 1:(n-1)) {
      for ( j in (i+1):n) {
        control <- 10^(-k)
        if( abs(a[i,j]) > control) 
        {
          #print(c(a[i,j],control))
          angulo <- 0.5*atan(2*a[i,j]/(a[i,i] - a[j,j]))
          c<-cos(angulo)
          s<-sin(angulo)
          p<-id
          p[i,i]<-c
          p[j,j]<-c
          p[i,j]<- s
          p[j,i]<- s
          Q <- Q%*%p
          a<-t(p)%*%a%*%p
          a[i,j]<-0
          a[j,i]<-0
        }
      }
    }
    print(a)
  }
  
  cat("\n")  
  cat("\n")
  cat("\n")
  #return(list(raices=diag(a),vectores=Q,estado=a))
}
alpha <- 5
beta  <- 3
B = matrix(c(2,0,-1,1,beta,2,-1,2,-1,1,alpha,1,0,0,0,0), ncol=4, byrow= TRUE)
print(B)
jacobi(B,10)
