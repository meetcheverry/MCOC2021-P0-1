from scipy import matrix, rand, linalg, half
from time import perf_counter
from matplotlib import pyplot as plt
from laplaciana import laplaciana
import numpy as np
import scipy as sp

tiempo = [[],[],[],[],[],[],[],[],[],[]]
memoria = [[],[],[],[],[],[],[],[],[],[]]
nm = [2, 5, 10,12, 15, 20,30, 40, 45, 50, 55,60, 75, 100,125, 160, 200,250, 350, 500,600, 800, 1000,2000, 5000, 10000]
 #dimension de matrices

for i in range(0,10):
    for N in nm:
        A = laplaciana(N,half)
        t1 = perf_counter()
        C = sp.linalg.inv(A,overwrite_a=False)
        t2=perf_counter() 

        dt = t2 - t1
        mem = A.nbytes + C.nbytes

        tiempo[i].append(dt)
        memoria[i].append(mem)


#grafica memoria
plt.plot(nm,memoria[0],nm,memoria[1],nm,memoria[2],nm,memoria[3],nm,memoria[4],nm,memoria[5],nm,memoria[6],nm,memoria[7],nm,memoria[8],nm,memoria[9])
#etiqueta ejes
plt.xlabel("Dimension matriz N")
plt.ylabel("Memoria utilizada")
#Titulo
plt.title("Rendimiento Caso 2,Half(A)")
#malla
plt.grid(True)
#mostrar grafico
plt.show()

#grafica tiempo 22

plt.plot(nm,tiempo[0],nm,tiempo[1],nm,tiempo[2],nm,tiempo[3],nm,tiempo[4],nm,tiempo[5],nm,tiempo[6],nm,tiempo[7],nm,tiempo[8],nm,tiempo[9])
#etiqueta ejes
plt.xlabel("Dimension matriz N")
plt.ylabel("Tiempo transcurrido [s]")
#Titulo
plt.title("Rendimiento Caso 2,Half(A)")
#malla
plt.grid(True)
#mostrar grafico
plt.show()