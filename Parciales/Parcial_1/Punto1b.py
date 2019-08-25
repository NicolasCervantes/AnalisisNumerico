import matplotlib.pyplot as plt

def sumaElementos(x, n):
  suma=0
  data=[]
  for i in range(n):
    for j in range(n):
      suma+=x[i][j]
      data.append(suma)
  plt.plot(data)
  plt.ylabel('Convergencia')
  plt.show()

A=[[3,4,5],[1,9,12],[1,9,2]]
sumaElementos(A,3)
