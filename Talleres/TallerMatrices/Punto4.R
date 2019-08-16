gauss = function(A, b)
{  
  n = nrow(A) 
  Ab = cbind(A,b)
  mult <- 0
  for (k in 1:(n-1))
  {   
    if(Ab[k,k]==0)
    {
      fila = which(Ab[k, ]!=0)[1]
      Ab[c(k, fila),  ] = Ab[c(fila, k),  ]
      mult <- mult +1
    }
    for (i in (k+1):n)
    {
      Ab[i, ] = Ab[i, ] - Ab[i, k]/Ab[k,k]*Ab[k, ]
      mult <- mult +1
    } 
  }
  x = rep(NA, times=n)
  x[n] = Ab[n, n+1]/Ab[n,n] 
  for(i in(n-1):1)
  {
    x[i]= (Ab[i, n+1]-sum(Ab[i,(i+1):n]*x[(i+1):n]))/Ab[i,i]
    mult <- mult +1
  }
  
  cat("multiplicaciones : ",mult,"\n")
  
  return(x) 
}
A = matrix(c( 0,  2,  3, 3,
              -5, -4,  1, 4,
              0,  0,  0, 3,
              -4, -7, -8, 9), nrow=4, byrow=TRUE)
b = c(1,0,0,0)
gauss(A,b)
