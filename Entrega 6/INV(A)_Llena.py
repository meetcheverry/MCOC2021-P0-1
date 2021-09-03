import numpy as np
import scipy as sp
from scipy import matrix, single, linalg
import matplotlib.pyplot as plt
from numpy import double
from time import perf_counter
from laplaciana import laplaciana_llena 
from laplaciana import laplaciana_dispersa 

#NUMERO DE CORRIDAS  
Ncorridas=5

#TAMAÑO DE MATRICES A PROBAR PARA CADA CORRIDA

U1       = []
nm = [2,4,10,11,13,15,20,30,40,45,50,55,60,75,80,100,200,500, 1000 , 2000 , 5000 , 10000]
tiempo_ens    = [[],[],[],[],[],[],[],[],[],[]]
tiempo1_ens   = []
tiempo_sol    = [[],[],[],[],[],[],[],[],[],[]]
tiempo1_sol   = []

C_1           = []
C_2           = []

N1_1          = []
N2_1          = []
N3_1          = []
N4_1          = []

N1_2          = []
N2_2          = []
N3_2          = []
N4_2          = []

#CREANDO ARCHIVOS DE TEXTO PARA CADA CORRIDA 
#Caso 1
for i in range(0,10):
    for N in nm:
        
        t1 = perf_counter()
        
        A = laplaciana_llena(N,double)
        b = np.ones(N,double)
        
        t2=perf_counter() 

        x= np.linalg.inv(A)

        t3=perf_counter()
        
        dt = t2 - t1       # Tiempo ensamblado
        dt2 = t3 - t2      # Tiempo Solucion

        tiempo_ens[i].append(dt/10)
        tiempo_sol[i].append(dt2/10)
        if i==0:
            tiempo1_ens.append(0)
            tiempo1_sol.append(0)

        print("corrida:",i,"/      N matriz:", N,"/   Tiempo:" ,dt ,dt2)  

f=open("Datos_Llena_INV_ens.txt","w")


for i in tiempo_ens:
    print(i)
    for j in i:
        print (j)
        f.write("\t"+str(j)+"\n")
f.close()

f=open("Datos_Llena_INV_Sol.txt","w")


for i in tiempo_sol:
    for j in i:
        f.write("\t"+str(j)+"\n")
f.close()


#Promedio de tiempo ensamblaje
for i in tiempo_ens:
    for j in range(len(nm)):
        tiempo1_ens[j]=tiempo1_ens[j]+i[j]

#Promedio de tiempo solucion
for i in tiempo_sol:
    for j in range(len(nm)):
        tiempo1_sol[j]=tiempo1_sol[j]+i[j]

#Funciones Para Ensamblaje

for i in nm:

    C_1.append(tiempo1_ens[len(nm)-1])
    N1_1.append((tiempo1_ens[len(nm)-1]/10000)*(i))
    N2_1.append((tiempo1_ens[len(nm)-1]/10000**2)*(i**2))
    N3_1.append((tiempo1_ens[len(nm)-1]/10000**3)*(i**3))
    N4_1.append((tiempo1_ens[len(nm)-1]/10000**4)*(i**4))

    C_2.append(tiempo1_sol[len(nm)-1])
    N1_2.append((tiempo1_sol[len(nm)-1]/10000)*(i))
    N2_2.append((tiempo1_sol[len(nm)-1]/10000**2)*(i**2))
    N3_2.append((tiempo1_sol[len(nm)-1]/10000**3)*(i**3))
    N4_2.append((tiempo1_sol[len(nm)-1]/10000**4)*(i**4))

# Imprimir Datos







print(C_1)
print(tiempo1_ens)
print(tiempo1_sol)


x1 = [10 , 20 , 50 , 100 , 200 , 500 ,1000, 2000, 5000,10000,100000]
xticks_txt1 = ["10", "20", "50", "100", "200", "500", "1000","2000", "5000","10000","100000"]
y1 = [0.1e-3, 1e-3, 1e-2, 0.1, 1., 10., 60, 600, 3600]
yticks_txt1 = ["0.1 ms", "1 ms", "10 ms", "0.1 s", "1 s", "10 s", "1 min", "10 min", "1 h"]
#grafica ensamblado
plt.subplot(2,1,1)
plt.loglog(nm,tiempo1_ens, color='k')
plt.loglog(nm,C_1,linestyle='--',label="C")
plt.loglog(nm,N1_1,linestyle='--',label="N")
plt.loglog(nm,N2_1,linestyle='--',label="N2")
plt.loglog(nm,N3_1,linestyle='--',label="N3")
plt.loglog(nm,N4_1,linestyle='--',label="N4")

#etiqueta ejes
plt.xlabel("Dimension matriz N")
plt.ylabel("Tiempo transcurrido (s)")
#Titulo
plt.xticks(x1 ,xticks_txt1, rotation = 45)
plt.yticks(y1, yticks_txt1)
plt.title("Tiempo de ensamblado INV(A)*b"
plt.ylim([0.000001, 600])
plt.xlim([0, 10000])

#malla
plt.grid(True)
plt.legend(loc=0)

#grafica rendimiento
plt.subplot(2,1,2)
plt.loglog(nm,tiempo1_sol, color='k')
plt.loglog(nm,C_2,linestyle='--',label="C")
plt.loglog(nm,N1_2,linestyle='--',label="N")
plt.loglog(nm,N2_2,linestyle='--',label="N2")
plt.loglog(nm,N3_2,linestyle='--',label="N3")
plt.loglog(nm,N4_2,linestyle='--',label="N4")
#etiqueta ejes
plt.xlabel("Dimension matriz N")
plt.ylabel("Tiempo transcurrido (s)")
#Titulo
plt.xticks(x1 ,xticks_txt1, rotation = 45)
plt.yticks(y1, yticks_txt1)
plt.title("Tiempo de solucion INV(A)")
plt.ylim([0.000001, 600])
plt.xlim([0, 10000])
#malla
plt.grid(True)
plt.legend(loc=0)
#mostrar grafico
plt.show()