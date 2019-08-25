import matplotlib.pyplot as plt

def sumaTriangular(A):
    matrix = list(list(A))
    n = len(matrix)
    suma = 0
    data=[]
    n = 0
    for x in range(0,n):
        for y in range(x,n):
            suma+=matrix[x][y]
            n += 1
            data.append(suma)
    plt.plot(data)
    plt.ylabel('Convergencia')
    plt.show()
    return suma

    
matrizA = [[1,2,3,5],[0,1,8,7],[0,0,8,5],[0,1,7,3]]
sumaTriangular(matrizA)
