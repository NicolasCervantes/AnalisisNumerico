#Calcula el error absoluto y relativo de una multiplicación

def errorDist(v, t, ev, et):
    distancia = v * t
    eAbsoluto = v * et + t * ev
    eRelativo = (ev / v) + (et / t)
    
    print("Distancia de la particula con el error absoluto: " + str(distancia) + " +/- " + str(eAbsoluto))
    print("Error relativo: ", eRelativo)

if __name__ == "__main__":
    errorDist(4, 5, 0.1, 0.1)
