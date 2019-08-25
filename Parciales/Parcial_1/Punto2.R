#Punto 2 parcial

rm(list=ls())

Fx = function(x) log(x+2)-sin(x)

ecuacion = function(x1, x2, error){
  x = seq(-2, 5, 0.1)
  plot(x, Fx(x), type = "l", col="green")
  x = x1-((Fx(x1))*(x1-x2)) / (Fx(x1) - Fx(x2))
  err = 1
  contador = 0
  while (err > error){
    contador = contador + 1
    x1 = x2
    x2 = x
    x = x1-((Fx(x1))*(x1-x2)) / (Fx(x1) - Fx(x2))
    err = abs((x-x2)/x)*100
    cat("Valor X: ", x, "\t\tValor del Error: ", err, "\t\tIteracion: ", contador, "\n")
  }
}

ecuacion(0,5, 10e-8)
