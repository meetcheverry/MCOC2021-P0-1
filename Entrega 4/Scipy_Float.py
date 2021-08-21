from scipy import matrix, single, linalg
from  time import perf_counter
from random import randint
from matplotlib import pyplot as plt
import numpy as np
import scipy as sp
from laplaciana import laplaciana
import pandas


U1       = []
U2       = []
U3       = []
U4       = []
U5       = []
U6       = []
U7       = []
U8       = []
U9   , U9b  = [],[]
U10  , U10b = [],[]
U11  , U11b = [],[]
U12  , U12b = [],[]

tiempo    = [[],[],[],[],[],[],[],[],[],[]]
tiempo1   = []
tiempo2   = []
tiempo3   = []
tiempo4   = []
tiempo5   = []
tiempo6   = []
tiempo7   = []
tiempo8   = []
tiempo9,  tiempo9b   = [],[]
tiempo10, tiempo10b  = [],[]
tiempo11, tiempo11b  = [],[]
tiempo12, tiempo12b  = [],[]


nm = [2, 5, 10,12, 15, 20,30, 40, 45, 50, 55, 60, 75, 100, 125, 160, 200, 350, 600, 1000,2000, 5000]
nm2 = [2, 5, 10,12, 15, 20,30, 40, 45, 50, 55, 60, 75, 100, 125, 160, 200, 350, 600, 1000]
 #dimension de matrices
     
#Caso 1
for i in range(0,10):
    for N in nm:
        
        A = laplaciana(N,single)
        b=np.ones(N)
        t1 = perf_counter()
        x= np.linalg.inv(A) * b
        t2=perf_counter() 

        dt = t2 - t1

        tiempo[i].append(dt)
        if i==0:
            tiempo1.append(0)


for i in range(0,(len(tiempo))):
    for j in range(0,(len(tiempo[0]))):
       
        tiempo1[j]+=(tiempo[i][j]/10)
tiempo = [[],[],[],[],[],[],[],[],[],[]]
#Caso 2
for i in range(0,10):
    for N in nm:
        
        A = laplaciana(N,single)
        b=np.ones(N)
        t1 = perf_counter()
        C= sp.linalg.solve(A,b)
        t2=perf_counter() 

        dt = t2 - t1
        mem = A.nbytes + C.nbytes

        tiempo[i].append(dt)
        if i==0:
            tiempo2.append(0)
for i in range(0,(len(tiempo))):
    for j in range(0,(len(tiempo[0]))):
       
        tiempo2[j]+=(tiempo[i][j]/10)
tiempo = [[],[],[],[],[],[],[],[],[],[]]
#Caso 3
for i in range(0,10):
    for N in nm:
        
        A = laplaciana(N,single)
        b=np.ones(N)
        t1 = perf_counter()
        C= sp.linalg.solve(A,b,assume_a='pos')
        
        t2=perf_counter() 

        dt = t2 - t1

        tiempo[i].append(dt)
        if i==0:
            tiempo3.append(0)
for i in range(0,(len(tiempo))):
    for j in range(0,(len(tiempo[0]))):
       
        tiempo3[j]+=(tiempo[i][j]/10)
tiempo = [[],[],[],[],[],[],[],[],[],[]]

#Caso 4
for i in range(0,10):
    for N in nm:
        
        A = laplaciana(N,single)
        b=np.ones(N)
        t1 = perf_counter()
        C= sp.linalg.solve(A,b,assume_a='sym')
        t2=perf_counter() 

        dt = t2 - t1

        tiempo[i].append(dt)
        if i==0:
            tiempo4.append(0)
for i in range(0,(len(tiempo))):
    for j in range(0,(len(tiempo[0]))):
       
        tiempo4[j]+=(tiempo[i][j]/10)
tiempo = [[],[],[],[],[],[],[],[],[],[]]

#Caso 5
for i in range(0,10):
    for N in nm:
        
        A = laplaciana(N,single)
        b=np.ones(N)
        t1 = perf_counter()
        C= sp.linalg.solve(A,b,overwrite_a=True)
        t2=perf_counter() 

        dt = t2 - t1
        mem = A.nbytes + C.nbytes

        tiempo[i].append(dt)
        if i==0:
            tiempo5.append(0)
for i in range(0,(len(tiempo))):
    for j in range(0,(len(tiempo[0]))):
       
        tiempo5[j]+=(tiempo[i][j]/10)
tiempo = [[],[],[],[],[],[],[],[],[],[]]

#Caso 6
for i in range(0,10):
    for N in nm:
        
        A = laplaciana(N,single)
        b=np.ones(N)
        t1 = perf_counter()
        C= sp.linalg.solve(A,b,overwrite_b=True)
        t2=perf_counter() 

        dt = t2 - t1
        

        tiempo[i].append(dt)
        if i==0:
            tiempo6.append(0)
for i in range(0,(len(tiempo))):
    for j in range(0,(len(tiempo[0]))):
       
        tiempo6[j]+=(tiempo[i][j]/10)
tiempo = [[],[],[],[],[],[],[],[],[],[]]

#Caso 7
for i in range(0,10):
    for N in nm:
        
        A = laplaciana(N,single)
        b=np.ones(N)
        t1 = perf_counter()
        C= sp.linalg.solve(A,b,overwrite_b=False,overwrite_a=True)
        t2=perf_counter() 

        dt = t2 - t1
        
        tiempo[i].append(dt)
        if i==0:
            tiempo7.append(0)
for i in range(0,(len(tiempo))):
    for j in range(0,(len(tiempo[0]))):
       
        tiempo7[j]+=(tiempo[i][j]/10)
tiempo = [[],[],[],[],[],[],[],[],[],[]]

#Caso 8
for i in range(0,10):
    for N in nm2:
        
        A = laplaciana(N,single)
        t1 = perf_counter()
        C= sp.linalg.eigh(A)
        t2=perf_counter() 

        dt = t2 - t1

        tiempo[i].append(dt)
        if i==0:
            tiempo8.append(0)

for i in range(0,(len(tiempo))):
    for j in range(0,(len(tiempo[0]))):
       
        tiempo8[j]+=(tiempo[i][j]/10)
tiempo = [[],[],[],[],[],[],[],[],[],[]]
print("llegue a eight")
#Caso 9
for i in range(0,10):
    for N in nm2:
        
        A = laplaciana(N,single)
        t1 = perf_counter()
        C= sp.linalg.eigh(A, driver="ev",overwrite_a=False)
        t2=perf_counter() 

        dt = t2 - t1
        print("1 corrida")

        tiempo[i].append(dt)
        if i==0:
            tiempo9.append(0)
for i in range(0,(len(tiempo))):
    for j in range(0,(len(tiempo[0]))):
       
        tiempo9[j]+=(tiempo[i][j]/10)
tiempo = [[],[],[],[],[],[],[],[],[],[]]

for i in range(0,10):
    for N in nm2:
        
        A = laplaciana(N,single)
        t1 = perf_counter()
        C= sp.linalg.eigh(A, driver="ev",overwrite_a=True)
        t2=perf_counter() 

        dt = t2 - t1


        tiempo[i].append(dt)
        if i==0:
            tiempo9b.append(0)
for i in range(0,(len(tiempo))):
    for j in range(0,(len(tiempo[0]))):
       
        tiempo9b[j]+=(tiempo[i][j]/10)

tiempo = [[],[],[],[],[],[],[],[],[],[]]

#Caso 10
for i in range(0,10):
    for N in nm2:
        
        A = laplaciana(N,single)
        t1 = perf_counter()
        C= sp.linalg.eigh(A, driver="evd",overwrite_a=True)
        t2=perf_counter() 

        dt = t2 - t1


        tiempo[i].append(dt)
        if i==0:
            tiempo10.append(0)
for i in range(0,(len(tiempo))):
    for j in range(0,(len(tiempo[0]))):
       
        tiempo10[j]+=(tiempo[i][j]/10)
tiempo = [[],[],[],[],[],[],[],[],[],[]]

#Parte b

for i in range(0,10):
    for N in nm2:
        
        A = laplaciana(N,single)
        t1 = perf_counter()
        C= sp.linalg.eigh(A, driver="evd",overwrite_a=False)     
        t2=perf_counter() 

        dt = t2 - t1
        

        tiempo[i].append(dt)
        if i==0:
            tiempo10b.append(0)
for i in range(0,(len(tiempo))):
    for j in range(0,(len(tiempo[0]))):
       
        tiempo10b[j]+=(tiempo[i][j]/10)
tiempo = [[],[],[],[],[],[],[],[],[],[]]

#Caso 11
for i in range(0,10):
    for N in nm2:
        
        A = laplaciana(N,single)
        t1 = perf_counter()
        C= sp.linalg.eigh(A, driver="evr",overwrite_a=True)
        t2=perf_counter() 

        dt = t2 - t1


        tiempo[i].append(dt)
        if i==0:
            tiempo11.append(0)
for i in range(0,(len(tiempo))):
    for j in range(0,(len(tiempo[0]))):
       
        tiempo11[j]+=(tiempo[i][j]/10)
tiempo = [[],[],[],[],[],[],[],[],[],[]]

#Parte b

for i in range(0,10):
    for N in nm2:
        
        A = laplaciana(N,single)
        t1 = perf_counter()
        C= sp.linalg.eigh(A, driver="evr",overwrite_a=False)
        t2=perf_counter() 

        dt = t2 - t1

        tiempo[i].append(dt)
        if i==0:
            tiempo11b.append(0)

for i in range(0,(len(tiempo))):
    for j in range(0,(len(tiempo[0]))):
       
        tiempo11b[j]+=(tiempo[i][j]/10)
tiempo = [[],[],[],[],[],[],[],[],[],[]]



#Caso 12
for i in range(0,10):
    for N in nm2:
        
        A = laplaciana(N,single)
        t1 = perf_counter()
        C= sp.linalg.eigh(A, driver="evx",overwrite_a=True)
        t2=perf_counter() 

        dt = t2 - t1

        tiempo[i].append(dt)
        if i==0:
            tiempo12.append(0)

for i in range(0,(len(tiempo))):
    for j in range(0,(len(tiempo[0]))):
       
        tiempo12[j]+=(tiempo[i][j]/10)
tiempo = [[],[],[],[],[],[],[],[],[],[]]

#Parte b

for i in range(0,10):
    for N in nm2:
        
        A = laplaciana(N,single)
        t1 = perf_counter()
        C= sp.linalg.eigh(A, driver="evx",overwrite_a=False)
        t2=perf_counter() 

        dt = t2 - t1


        tiempo[i].append(dt)
        if i==0:
            tiempo12b.append(0)

for i in range(0,(len(tiempo))):
    for j in range(0,(len(tiempo[0]))):
       
        tiempo12b[j]+=(tiempo[i][j]/10)



print(len(tiempo1))
print(len(tiempo2))
print(len(tiempo3))
print(len(tiempo4))
print(len(tiempo5))
print(len(tiempo6))
print(len(tiempo7))
print(len(tiempo8))
print(len(tiempo9))
print(len(tiempo9b))
print(len(tiempo10))
print(len(tiempo10b))
print(len(tiempo11))
print(len(tiempo11b))
print(len(tiempo12))
print(len(tiempo12b))



# Sacar promedio

#Escribir archivos en txt

f=open("Datos_solve.txt","w")


for i in tiempo1:
    f.write("\t"+str(i)+"\n")

for i in tiempo2:
    f.write("\t"+str(i)+"\n")

for i in tiempo3:
    f.write("\t"+str(i)+"\n")

for i in tiempo4:
    f.write("\t"+str(i)+"\n")

for i in tiempo5:
    f.write("\t"+str(i)+"\n")

for i in tiempo6:
    f.write("\t"+str(i)+"\n")

for i in tiempo7:
    f.write("\t"+str(i)+"\n")

for i in tiempo8:
    f.write("\t"+str(i)+"\n")

for i in tiempo9:
    f.write("\t"+str(i)+"\n")

for i in tiempo9b:
    f.write("\t"+str(i)+"\n")

for i in tiempo10:
    f.write("\t"+str(i)+"\n")

for i in tiempo10b:
    f.write("\t"+str(i)+"\n")

for i in tiempo11:
    f.write("\t"+str(i)+"\n")

for i in tiempo11b:
    f.write("\t"+str(i)+"\n")

for i in tiempo12:
    f.write("\t"+str(i)+"\n")
 
for i in tiempo12b:
    f.write("\t"+str(i)+"\n")
 


f.close()

#Extraer datos de txt

file="Datos_solve.txt"
data=pandas.read_fwf(file,sep='\t',header= None)

for i in range(0,(len(tiempo1)-1)):
    U1.append(  data.iat[i,0                      ])
    U2.append(  data.iat[(i+len(tiempo1)),0       ])
    U3.append(  data.iat[(i+2*len(tiempo2)),0     ])
    U4.append(  data.iat[(i+3*len(tiempo3)),0     ])
    U5.append(  data.iat[(i+4*len(tiempo4)),0     ])
    U6.append(  data.iat[(i+5*len(tiempo5)),0     ])
    U7.append(  data.iat[(i+6*len(tiempo6)),0     ])
    U8.append(  data.iat[(i+7*len(tiempo7)),0     ])
    U9.append(  data.iat[(i+7*len(tiempo8)+len(tiempo8)),0     ])
    U12b.append(data.iat[(i+7*len(tiempo8)+8*len(tiempo9)),0    ])
    U9b.append( data.iat[(i+7*len(tiempo8)+2*len(tiempo9b)),0     ])
    U10.append( data.iat[(i+7*len(tiempo8)+3*len(tiempo10)),0     ])
    U10b.append(data.iat[(i+7*len(tiempo8)+4*len(tiempo10b)),0     ])
    U11.append( data.iat[(i+7*len(tiempo8)+5*len(tiempo11)),0    ])
    U11b.append(data.iat[(i+7*len(tiempo8)+6*len(tiempo11b)),0    ])
    U12.append( data.iat[(i+7*len(tiempo8)+7*len(tiempo12)),0    ])

print(U1,len(U1))
print(U2,len(U2))
print(U3,len(U3))
print(U4,len(U4))
print(U5,len(U5))
print(U6,len(U6))
print(U7,len(U7))
print(U8,len(U8))
print(U9,len(U9))
print(U9,len(U9))
print(U10,len(U10))
print(U10b,len(U10b))
print(U11,len(U11))
print(U11b,len(U11b))
print(U12,len(U12))
print(U12b,len(U12b))




#Graficos Comparativos
#plt.plot(tamano,tiempo,marker="o")

# Comparacion 1 Ax=b

plt.loglog(nm,tiempo1,label="inv(A)*B                         ")
plt.loglog(nm,tiempo2,label="sp.linal.solve(A,b)              ")
plt.loglog(nm,tiempo3,label="assume_a=pos                     ")
plt.loglog(nm,tiempo4,label="assume_a=sym                     ")
plt.loglog(nm,tiempo5,label="overwrite_a=True                 ")
plt.loglog(nm,tiempo6,label="overwrite_b=True                 ")
plt.loglog(nm,tiempo7,label="overwrite_a=True,overwrite_b=True")
        
xTicks = [10,20,50,100,200,500,1000,2000,5000,10000]
xTicks_Text = ["10","20","50","100","200","500","1000",
                        "2000","5000","10000"]
        
yTicks = [10**-4,10**-3,10**-2,10**-1,1,10,60,600]
yTicks_Text = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10min"]
        
plt.yticks(yTicks, yTicks_Text)
plt.xticks(xTicks, xTicks_Text,rotation=45)
        
plt.title("Desempeño", fontsize=10)
plt.ylabel("Tiempo transcurrido")
plt.xlabel("Tamaño matriz N")


plt.grid(True)
plt.legend()    
plt.tight_layout()           
plt.show() 


# Comparacion 2 Valores propios

plt.loglog(nm2,tiempo8,label=  "Parametros Normales               ")
plt.loglog(nm2,tiempo9,label = "driver= ev y overwrite_a=True     ")
plt.loglog(nm2,tiempo9b,label= "driver= ev y overwrite_a=False    ")
plt.loglog(nm2,tiempo10,label= "driver= evd y overwrite_a=True    ")
plt.loglog(nm2,tiempo10b,label="driver= evd y overwrite_a=False   ")
plt.loglog(nm2,tiempo11,label= "driver= evr y overwrite_a=True    ")
plt.loglog(nm2,tiempo11b,label="driver= evr y overwrite_a=False   ")
plt.loglog(nm2,tiempo12,label= "driver= evx y overwrite_a=True    ")
plt.loglog(nm2,tiempo12b,label="driver= evx y overwrite_a=False   ")
        
xTicks = [10,20,50,100,200,500,1000,2000]
xTicks_Text = ["10","20","50","100","200","500","1000",
                        "2000"]
        
yTicks = [10**-4,10**-3,10**-2,10**-1,1,10,60,600]
yTicks_Text = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10min"]
        
plt.yticks(yTicks, yTicks_Text)
plt.xticks(xTicks, xTicks_Text,rotation=45)
        
plt.title("Desempeño Valores Propios", fontsize=10)
plt.ylabel("Tiempo transcurrido")
plt.xlabel("Tamaño matriz N")


plt.grid(True)
plt.legend()    
plt.tight_layout()           
plt.show() 