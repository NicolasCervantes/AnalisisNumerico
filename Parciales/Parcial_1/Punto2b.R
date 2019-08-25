#Punto 2b parcial

rm(list=ls())

Fx = function(x) log(x+2)-sin(x)#exp(x) - pi * x
ecuacion = function(x, x1, error){
  x = seq(-2, 5, 0.1)
    plot(x, Fx(x), type = "l", col="blue")
  x2= x1-((Fx(x1))*(x1-x)) / (Fx(x1) - Fx(x))
  err = 1
  contador = 0
  while (err > error){
    contador = contador + 1
    if(Fx(x2)&& Fx(x1)<0){
    x2= x1
    x1=x
    }
    else{
      x2=x1
    }
    x2= x1-((Fx(x1))*(x1-x)) / (Fx(x1) - Fx(x))
    err = abs((x2-x1)/x2)*100
    cat("Valor X: ", x, "\t\tValor del Error: ", err, "\t\tIteracion: ", contador, "\n")
  }
}

ecuacion(-1,5, 10e-8)
