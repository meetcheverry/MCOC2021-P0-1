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

# Desempeño INV(A)

## Caso 1: numpy.linalg.inv()
### dtype=np.half
* ERROR: ARRAY TYPE FLOAT16 UNSUPPORTED IN LINALG
### dtype=np.single
![](/Graf_Caso1_Single)
![](/Graf_Caso1_Single_Tiempo)
### dtype=np.double
![](/Graf_Caso1_Double)
![](/Graf_Caso1_Double_Tiempo)
### dtype=np.longdouble
* ERROR: ARRAY TYPE FLOAT64 UNSUPPORTED IN LINALG

## Caso 2: scipy.linalg.inv(overwrite_a=False)
### dtype=np.half
![](/Graf_Caso2_Half)
![](/Graf_Caso2_Half_Tiempo)
### dtype=np.single
![](/Graf_Caso2_Single)
![](/Graf_Caso2_Single_Tiempo)
### dtype=np.double
![](/Graf_Caso2_Double)
![](/Graf_Caso2_Double_Tiempo)
### dtype=np.longdouble
![](/Graf_Caso2_LongDouble)
![](/Graf_Caso2_Longdouble_Tiempo)
## Caso 3: scipy.linalg.inv(overwrite_a=True)
### dtype=np.half
![](/Graf_Caso3_Half)
![](/Graf_Caso3_Half_Tiempo)
### dtype=np.single
![](/Graf_Caso3_Double)
![](/Graf_Caso3_Double_Tiempo)
### dtype=np.double
![](/Graf_Caso3_Double)
![](/Graf_Caso3_Double_Tiempo)
### dtype=np.longdouble
![](/Graf_Caso3_Longdouble)
![](/Graf_Caso3_LongDouble_Tiempo)

* Es evidente y comprobable que en los 4 tipos de datos: Half, single, double y 
  longdouble hay diferencias en cuanto a la precisión de números, siendo half el menos
  preciso, aguantando números no tan extensos, y longdouble el más preciso. Con esa 
  lógica, se observa un proporcionalidad en cuanto a un mayor tiempo de procesamiento 
  en los tipos de datos más precisos y un menor tiempo en los menos precisos. Por 
  ejemplo, en el caso 3 se observó que para matrices (10.000 x 10.000), el dtype=np.half
  demoró 39,218 (s) en calcular la inversa, en cambio el dtype=np.longdouble, demoró
  58,675 (s) y los 2 ocuparon 1,6 GB se memoria.Esre tipo de ejemplos se repitio, por lo
  que es posible inferir que +precision = +tiempo pero no necesariamente +memoria.
* ¿Qué algoritmo de inversión cree que utiliza cada método?
   Se utiliza la solución analítica, de la regla de Cramer y teorema de Laplace, que
   basa el calculo del determinante de matrices grandes en la descomposición de sumas 
   de matrices más pequeñas. 
* ¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño 
  en cada caso? El paralelismo es una funcionalidad que permite realizar operaciones
  simultaneamente y buscar información en los distintos niveles de cachés del procesador,
  en mi caso tengo 3 niveles: L1: 384 KB, L2: 2 MB, L3: 4 MB, que se muestran en los 
  gráficos con lineas horizontales negras. Estas permiten regular la eficiencia con la 
  que se opera, las de menor memoria operan más rápido, como la caché 3.

