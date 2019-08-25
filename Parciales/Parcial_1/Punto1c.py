import matplotlib.pyplot as plt

def primerosCuadrados(n):
	suma=0
	data=[]
	for i in range(n):
		suma+=pow(i,2)
		data.append(suma)
	plt.plot(data)
  	plt.ylabel('Convergencia')
  	plt.show()

primerosCuadrados(5)
