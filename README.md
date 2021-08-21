# MCOC2021-P0

# Mi computador principal

* Marca/Modelo: hp OMEN 15
* Tipo: Notebook
* Año Adquisicion: 2021
* Procesador:
  * Marca/Modelo: intel Core i5-10300H
  * capacidad base: 2,5GHz
  * Velocidad Maxima: 3,9GHz
  * Numero de nucleos: 4
  * Numero de hilos: 8
  * Arquitectura: Nehalem
  * Set de instrucciones: 64-bit
* Tamaño de las caches del procesador
  * L1: 256 kb
  * L2: 1 mb
  * L3: 8 Mb
* Memoria
  * Total: 15.8 Gb
  * Tipo Memoria: DDR4
  * Velocidad Memoria: 2933 MHz
  * Numero de (SO)DIMM: 2
* Tarjeta Grafica
  * Marca/Modelo: Intel UHD Graphics
  * Meoria dedicada: NVIDIA GeForce RTX 2060
  * Resolucion: 1920 x 1080
* Disco Unico:
  * Marca: hp
  * Tipo: SSD
  * Tamaño: 500 GB
  * Particiones: 3
  * Sistema de archivos: NTFS
* Dirección MAC de la tarjeta wifi: 58-00-53-F1-31-3D
* Dirección IP (Interna, del router): 192.168.100.1 
* Dirección IP (Externa, del ISP): 181.43.140.65
* Proveedor de internet: Entel

# Entrega 3
# Desempeño INV(A)

## Caso 1: numpy.linalg.inv()
### dtype=np.half
* ERROR: ARRAY TYPE FLOAT16 UNSUPPORTED IN LINALG
### dtype=np.single

![](/Graf_Caso1_Single.png)
![](/Graf_Caso1_Single_Tiempo.png)

### dtype=np.double

![](/Graf_Caso1_Double.png)
![](/Graf_Caso1_Double_Tiempo.png)

### dtype=np.longdouble
* ERROR: ARRAY TYPE FLOAT64 UNSUPPORTED IN LINALG

## Caso 2: scipy.linalg.inv(overwrite_a=False)
### dtype=np.half

![](/Graf_Caso2_Half.png)
![](/Graf_Caso2_Half_Tiempo.png)

### dtype=np.single

![](/Graf_Caso2_Single.png)
![](/Graf_Caso2_Single_Tiempo.png)

### dtype=np.double

![](/Graf_Caso2_Double.png)
![](/Graf_Caso2_Double_Tiempo.png)

### dtype=np.longdouble

![](/Graf_Caso2_LongDouble.png)
![](/Graf_Caso2_Longdouble_Tiempo.png)

## Caso 3: scipy.linalg.inv(overwrite_a=True)

### dtype=np.half

![](/Graf_Caso3_Half.png)
![](/Graf_Caso3_Half_Tiempo.png)

### dtype=np.single

![](/Graf_Caso3_Double.png)
![](/Graf_Caso3_Double_Tiempo.png)

### dtype=np.double

![](/Graf_Caso3_Double.png)
![](/Graf_Caso3_Double_Tiempo.png)

### dtype=np.longdouble

![](/Graf_Caso3_Longdouble.png)
![](/Graf_Caso3_LongDouble_Tiempo.png)

* Los 4 tipos de datos: Half, single, double y 
  longdouble Difieren en cuanto a la precisión de números, siendo half el menos
  preciso, aguantando números no tan extensos, y longdouble el más preciso. Siguiendo esta informacion, se puede notar en los graficos que al aumentar la "calidad" de los numeros la memoria utilizada va a ser mayor al igual que el tiempo que toma el computador en procesar las operaciones. Podria ser util usar numeros mas extensos cuando es de suma importancia que la precision sea optima. 
* ¿Qué algoritmo de inversión cree que utiliza cada método? 
   Se utiliza la solución analítica, teorema de Laplace y regla de Cramer.   
* ¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño 
  en cada caso? El paralelismo es una funcionalidad que permite realizar operaciones
  simultaneamente y buscar información en los distintos niveles de cachés del procesador,
  en mi caso tengo 3 niveles: L1: 256 KB, L2: 1 MB, L3: 8 MB. Estas permiten regular la eficiencia con la 
  que se opera, las de menor memoria operan más rápido.


# Entrega 4

### Graficos comparativos con distintos metodos utilizando tipo de datos: Double
![](/Entrega%204/Grafico_Solve_Double_2.png)
![](/Entrega%204/Grafico_Eigh_Double_1.png)

### Graficos comparativos con distintos metodos utilizando tipo de datos: Single
![](/Entrega%204/Grafico_Solve_single_1.png)
![](/Entrega%204/Grafico_Eigh_single_1.png)


### Comentarios Ax=b 
* El caso mas lento para resolver este problemas sin dudas es de invertir la matriz y luego multiplicar, mientras mayor sean las matrices, mas se demora respecto a suss pares. El mas rapido de todos los casos seria assume "POS" el cual utiliza matrices definidas positivas, esta opcion baja el tiempo de solucion, aunque el tiempo es parecido con el resto de las opciones(sin considerar caso 1). En un principio La velocidad de resultado es variable para tamoños pequeños de matrices, el tiempo que demora el programa se ve mas determinado por el tiempo que toma el codigo en si en correr y no al desarrollo de la operacion matematica. Monitoreando el rendimiento del computador, lo que mas se utilizo fue el procesador, el alza de memoria no fue notorio.

### Comentarios V. propios
* En este caso los metodos mas veloces son: Parametros iniciales, driver=evr con y sin sobre escribir la matriz A, driver= evd con y sin overwrite. Por ultimo los casos mas lentos serian driver=evx y ev con y sin overwrite. En este caso no se noto diferencia al comparar con y sin sobre escribir la matriz, lo que no es muy confiable ya que al sobre escribir se deberia ahorar memoria y quizas con eso disminuir el timepo.
