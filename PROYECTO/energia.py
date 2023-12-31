# -*- coding: utf-8 -*-
"""Energia.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vKvxSoKytKxAAGpILQLSrKYP7ppiOqsH

# **Sistema de Control y Prevención**
    
![123.png](data:image/png;base64,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)

# Valores Pico de Energía(Wh)⚡ y Emisiones GEI(GgCO2eq) 🗺
"""

#-----------------------------------------------------------------------------
#Fuerza Bruta - Valores Pico
#Función que evalua cada elemento y añade los valores picos en un arreglo final
picos = []

def encuentraPico(arr, n) :
  # Si solo hay elemento
  if (n == 1) :
    return picos.append(n-1)

  #Si el primer elemento es mayor que el segundo
  if (arr[0] >= arr[1]) :
    picos.append(0)

  #Comprobar todos los demás elementos
  for i in range(0, n-1) :
    # Comprobar si los vecinos son más pequeños
    if (arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]):
      picos.append(i)

  #Si el último elemento es mayor que el penúltimo
  if (arr[n - 1] >= arr[n - 2]) :
    picos.append(n-1)

  return picos
#------------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Divide y Vencerás - Valor Pico
# Función basada en búsqueda binaria que devuelve el índice de un elemento pico

def encuentra_PicoB(arr, bajo, alto, n):

	# Encuentra el índice del elemento medio
	med = bajo + (alto - bajo)/2
	med = int(med)

	# Compara el elemento del medio con su vecinos (si existen vecinos)
	if ((med == 0 or arr[med - 1] <= arr[med]) and
	    (med == n - 1 or arr[med + 1] <= arr[med])):
		return med

	# Si el elemento medio no es pico y su vecino izquierdo es mayor
	# que eso, luego la mitad izquierda debe tener un elemento pico
	elif (med > 0 and arr[med - 1] > arr[med]):
		return encuentra_PicoB(arr, bajo, (med - 1), n)

	# Si el elemento medio no es pico y su vecino derecho es mayor
	# que eso, entonces la mitad derecha debe tener un elemento pico
	else:
		return encuentra_PicoB(arr, (med + 1), alto, n)

def encuentraPicoA(arr, n):
	return encuentra_PicoB(arr, 0, n - 1, n)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Para colocar etiquetas con valores al gráfico de barras
def add_value_labels(ax, spacing=5):
    """ ax (matplotlib.axes.Axes): El objeto que contiene ax del gráfico
        spacing (int): Distancia entre las etiquetas y las barras.
    """
    # For each bar: Place a label
    for rect in ax.patches:
        # Get X and Y placement of label from rect.
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        # Number of points between bar and label. Change to your liking.
        space = spacing
        # Vertical alignment for positive values
        va = 'bottom'

        # If value of bar is negative: Place label below bar
        if y_value < 0:
            # Invert space to place label below
            space *= -1
            # Vertically align label at top
            va = 'top'

        # Use Y value as label and format number with one decimal place
        label = "{:.1f}".format(y_value)

        # Create annotation
        ax.annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at end of the bar
            xytext=(0, space),          # Vertically shift label by `space`
            textcoords="offset points", # Interpret `xytext` as offset in points
            ha='center',                # Horizontally center label
            va=va)                      # Vertically align label differently for
                                        # positive and negative values.
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Main - Principal
# Lista Ciudadanos DNI
Dni = [76555487, 76555488, 18119550, 123456789, 789456123]
# Lista Ciudadanos Nombres
Nombre = ["Angely Mendez", "Ciara Mendez", "Berta Lopeez", "Juana Garcia", "Pablo Rojas"]
print( "Sistema de Control y Prevención - Energía y Emisiones GEI\n")
dni = input("Digite su número de DNI: ")
dni = int(dni)
if dni in Dni:
  print( "\nBienvenid@, ", Nombre[Dni.index(dni)])
  print( "\n 1. Ver todos los valores picos")
  print( "\n 2. Ver solo el máximo valor pico")
  print( "\n 3. Salir")
  opcion = input("\nDigite una opción: ")
  opcion = int(opcion)
else:
  ("\n-Ese número de DNI no existe")
#------------------------------------------------------------------------------


if opcion == 1:
  #------------------------------------------------------------------------------

  # Datos Desorden
  consumo = [5,254,3.1,101,0.9,145,272,199,909,299,104,334,102,5.1,1822,34.9,
           0.153,72,88,119,93,3.1,14,1,4]
  departamentos = ["AMAZONAS","ANCASH","APURIMAC","AREQUIPA","AYACUCHO",
                 "CAJAMARCA","CALLAO", "CUSCO", "HUANCAVELICA", "HUANUCO",
                 "ICA", "JUNIN   ", "LA LIBERTAD", "LAMBAYEQUE", "LIMA   ",
                 "LORETO", "MADRE DE DIOS", "MOQUEGUA", "PASCO", "PIURA    ",
                 "PUNO", "SAN MARTIN", "        TACNA   ", "TUMBES",
                 "        UCAYALI"]

  #------------------------------------------------------------------------------

  # Valores picos
  n = len(consumo)
  encuentraPico(consumo, n) #retorna arreglo con los índices de los valores pico
  picos.sort() #ordena en orden ascendente los valores pico
  k=len(picos)

  #------------------------------------------------------------------------------

  # Calcula las emisiones GEI
  # 2016, la producción total de energía eléctrica a nivel nacional totalizó 51,768 GWh OSINERGMIN
  # 2016, segundo sector con mayores emisiones de GEI reportada es Energía, con 58,132.54 GgCO2eq
  # 2016 -> Emisiones GEI = (consumo * 58,132.54 )/ 51,768 GgCO2eq
  contamina = []
  for i in range(0, n):
    contamina.append(round((consumo[i]* 58132.54)/ 51768,2))

  #------------------------------------------------------------------------------

  #Muestra Resultados - Fuerza Bruta
  print( "\n\n----------------------------------------")
  print( "Resultados Valores Pico: Diciembre 2021 ")
  print( "----------------------------------------\n")
  print( "Cantidad Total de Departamentos: ", n)
  print( "Total Nacional de Energía Eléctrica(GWh): ", sum(consumo))
  print( "Total Nacional de Emisiones GEI(GgCO2eq): ", sum(contamina))
  print( "Valores Picos de Energía: ", len(picos))
  print( "\n\nN°\tConsumo (GWh)\tDepartamentos    GEI aprox.(GgCO2eq)")
  print("-----------------------------------------------------------")
  suma1 = 0
  suma2 = 0
  for i in range(0,  k):
    a = picos[i]
    print( i+1, "\t   ", consumo[a], "\t", departamentos[a], "\t",contamina[a])
    suma1 = suma1 + consumo[a]
    suma2 = suma2 + contamina[a]

  print("-----------------------------------------------------------")
  print("Total:    ", suma1,"                        ",suma2)


if opcion == 2:
  #------------------------------------------------------------------------------

  # Datos ordenados
  consumo = [5,254,3.1,101,0.9,145,272,199,909,299,104,334,102,5.1,1822,34.9,0.153,72,88,119,93,3.1,14,1,4]
  consumo.sort() #ordenamiento
  departamentos = ["MADRE DE DIOS", "AYACUCHO", "TUMBES","SAN MARTIN","APURIMAC","        UCAYALI","AMAZONAS","LAMBAYEQUE","        TACNA   ","LORETO","MOQUEGUA","PASCO","PUNO","AREQUIPA","LA LIBERTAD","ICA","PIURA    ","CAJAMARCA","CUSCO","ANCASH","CALLAO", "HUANUCO","JUNIN   ","HUANCAVELICA",  "LIMA   "]

  #------------------------------------------------------------------------------

  # Muestra Valor pico
  m = len(consumo)
  p = encuentraPicoA(consumo, m) #retorna indice del valor pico

  #------------------------------------------------------------------------------

  #Muestra Resultados - Fuerza Bruta
  print( "\n\n----------------------------------------")
  print( "Resultados Máximo Valor Pico: Diciembre 2021 ")
  print( "----------------------------------------\n")
  print( "Cantidad Total de Departamentos: ", n)
  print( "Total Nacional de Energía Eléctrica(GWh): ", sum(consumo))
  print( "Total Nacional de Emisiones GEI(GgCO2eq): ", sum(contamina))
  print( "Valores Picos de Energía: ", len(picos))

  print( "\n\nN°\tConsumo (GWh)\tDepartamentos    GEI aprox.(GgCO2eq)")
  print("-----------------------------------------------------------")

  print( 1, "\t   ", consumo[p], "\t", departamentos[p], "\t",round((consumo[p]* 58132.54)/ 51768,2))

  print("-----------------------------------------------------------")
  print("Total:     ", consumo[p],"                       ",round((consumo[p]* 58132.54)/ 51768,2))

  #------------------------------------------------------------------------------

#------------------------------------------------------------------------------
print("\n\n\n\n")
# Grafico de Barras: para Depart. Vs Energia - Fuerza Bruta
from random import seed
import seaborn as sns
import matplotlib.pyplot as plt
seed(True)
sns.set(style="whitegrid")
plt.figure(figsize=(29,8)) # Cambia tamaño grafico ancho - largo
# Establece el título del gráfico
plt.title("Producción de Energía Eléctrica en los Departamentos del Perú - Año 2021 - Mes Diciembre")
plt.xlabel("Departamentos del Perú")   # Establece el título del eje x
plt.ylabel("Consumo de Energía Eléctrica G(Wh)")   # Establece el título del eje y
x=["AM","AN","AP","AR","AY","CA","CAL","CU","HU","HUA","ICA","JUN","LAL","LAM","LIM","LO","MA","MO","PA","PI","PU","SA","TA","TU","UC"]
y=[5,254,3.1,101,0.9,145,272,199,909,299,104,334,102,5.1,1822,34.9,0.153,72,88,119,93,3.1,14,1,4]
ax=sns.barplot(x=x, y=y)
add_value_labels(ax) #Etiquetas de valor gráfico
#solo dibuja línea sobre gráfico
plt.plot(x,y)
plt.show()

#------------------------------------------------------------------------------
print("\n\n\n\n")
# Grafico de Barras: para Depart. Vs GEI - Fuerza Bruta
seed(True)
sns.set(style="whitegrid")
plt.figure(figsize=(29,8)) # Cambia tamaño grafico ancho - largo
# Establece el título del gráfico
plt.title("Emisiones GEI en los Departamentos del Perú - Año 2021 - Mes Diciembre")
plt.xlabel("Departamentos del Perú")   # Establece el título del eje x
plt.ylabel("Emisiones GEI aprox.(GgCO2eq)")   # Establece el título del eje y
ax=sns.barplot(x=x,y=contamina)
#Etiquetas de valor gráfico
add_value_labels(ax)
#solo línea
plt.plot(x,contamina)
plt.show()

print("\n\n\n\n")
#------------------------------------------------------------------------------

"""#Fuerza Bruta - Valores Pico"""

#Fuerza Bruta - Valor Pico
picos = []

def encuentraPico(arr, n) :
  # Si solo hay elemento
  if (n == 1) :
    return picos.append(n-1)

  #Si el primer elemento es mayor que el segundo
  if (arr[0] >= arr[1]) :
    picos.append(0)

  #Comprobar todos los demás elementos
  for i in range(0, n-1) :
    # Comprobar si los vecinos son más pequeños
    if (arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]):
      picos.append(i)

  #Si el último elemento es mayor que el penúltimo
  if (arr[n - 1] >= arr[n - 2]) :
    picos.append(n-1)

  return picos

def add_value_labels(ax, spacing=5):
    """Add labels to the end of each bar in a bar chart.

    Arguments:
        ax (matplotlib.axes.Axes): The matplotlib object containing the axes
            of the plot to annotate.
        spacing (int): The distance between the labels and the bars.
    """

    # For each bar: Place a label
    for rect in ax.patches:
        # Get X and Y placement of label from rect.
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        # Number of points between bar and label. Change to your liking.
        space = spacing
        # Vertical alignment for positive values
        va = 'bottom'

        # If value of bar is negative: Place label below bar
        if y_value < 0:
            # Invert space to place label below
            space *= -1
            # Vertically align label at top
            va = 'top'

        # Use Y value as label and format number with one decimal place
        label = "{:.1f}".format(y_value)

        # Create annotation
        ax.annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at end of the bar
            xytext=(0, space),          # Vertically shift label by `space`
            textcoords="offset points", # Interpret `xytext` as offset in points
            ha='center',                # Horizontally center label
            va=va)                      # Vertically align label differently for
                                        # positive and negative values.

# Datos
consumo = [5,254,3.1,101,0.9,145,272,199,909,299,104,334,102,5.1,1822,34.9,
           0.153,72,88,119,93,3.1,14,1,4]
departamentos = ["AMAZONAS","ANCASH","APURIMAC","AREQUIPA","AYACUCHO",
                 "CAJAMARCA","CALLAO", "CUSCO", "HUANCAVELICA", "HUANUCO",
                 "ICA", "JUNIN   ", "LA LIBERTAD", "LAMBAYEQUE", "LIMA   ",
                 "LORETO", "MADRE DE DIOS", "MOQUEGUA", "PASCO", "PIURA    ",
                 "PUNO", "SAN MARTIN", "        TACNA   ", "TUMBES",
                 "        UCAYALI"]

# Muestra Valores picos
n = len(consumo)
encuentraPico(consumo, n) #retorna arreglo con los índices de los valores pico
picos.sort() #ordena en orden ascendente los valores pico
k=len(picos)
# 2016, la producción total de energía eléctrica a nivel nacional totalizó 51,768 GWh OSINERGMIN
# 2016, segundo sector con mayores emisiones de GEI reportada es Energía, con 58,132.54 GgCO2eq
# 2016 -> Emisiones GEI = (consumo * 58,132.54 )/ 51,768 GgCO2eq
print( "Producción de Energía Eléctrica\n")
print( "Cantidad de Departamentos: ",n)

#Graficar
from random import seed
import seaborn as sns
import matplotlib.pyplot as plt
seed(True)
#gráfico de barras
sns.set(style="whitegrid")
plt.figure(figsize=(29,8)) # Cambia tamaño grafico ancho - largo
plt.title("Producción de Energía Eléctrica en los Departamentos del Perú - Año 2021 - Mes Diciembre")   # Establece el título del gráfico
plt.xlabel("Departamentos del Perú")   # Establece el título del eje x
plt.ylabel("Consumo de Energía Eléctrica G(Wh)")   # Establece el título del eje y
x=["AM","AN","AP","AR","AY","CA","CAL","CU","HU","HUA","ICA","JUN","LAL","LAM","LIM","LO","MA","MO","PA","PI","PU","SA","TA","TU","UC"]
y=[5,254,3.1,101,0.9,145,272,199,909,299,104,334,102,5.1,1822,34.9,0.153,72,88,119,93,3.1,14,1,4]
ax=sns.barplot(x=x, y=y)
#Etiquetas de valor gráfico
add_value_labels(ax)
#solo línea
plt.plot(x,y)
plt.show()

print( "Resultados")
print( "----------\n")

contamina = []
for i in range(0, n):
  contamina.append(round((consumo[i]* 58132.54)/ 51768,2))

#gráfico de barras
seed(True)
sns.set(style="whitegrid")
plt.figure(figsize=(29,8)) # Cambia tamaño grafico ancho - largo
# Establece el título del gráfico
plt.title("Emisiones GEI en los Departamentos del Perú - Año 2021 - Mes Diciembre")
plt.xlabel("Departamentos del Perú")   # Establece el título del eje x
plt.ylabel("Emisiones GEI aprox.(GgCO2eq)")   # Establece el título del eje y
ax=sns.barplot(x=x,y=contamina)
#Etiquetas de valor gráfico
add_value_labels(ax)
#solo línea
plt.plot(x,contamina)
plt.show()


print( "Valores Picos de Energía\n")
print( "N°\tConsumo (GWh)\tDepartamentos    GEI aprox.(GgCO2eq)")
print("-----------------------------------------------------------")
suma1 = 0
suma2 = 0
for i in range(0,  k):
  a = picos[i]
  print( i+1, "\t   ", consumo[a], "\t", departamentos[a], "\t",contamina[a])
  suma1 = suma1 + consumo[a]
  suma2 = suma2 + contamina[a]

print("-----------------------------------------------------------")
print("Total:    ", suma1,"                        ",suma2)

"""#Divide y conquistar - Valor Pico"""

# Función basada en búsqueda binaria
# que devuelve el índice de un elemento pico

def encuentra_PicoB(arr, bajo, alto, n):
	#band = 0
	# Encuentra el índice del elemento medio
	med = bajo + (alto - bajo)/2
	med = int(med)

	# Compara el elemento del medio con su
	# vecinos (si existen vecinos)
	if ((med == 0 or arr[med - 1] <= arr[med]) and
	    (med == n - 1 or arr[med + 1] <= arr[med])):
		return med

	# Si el elemento medio no es pico y
	# su vecino izquierdo es mayor
	# que eso, luego la mitad izquierda debe
	# tener un elemento pico
	#if band == 1:
	elif (med > 0 and arr[med - 1] > arr[med]):
		return encuentra_PicoB(arr, bajo, (med - 1), n)

	# Si el elemento medio no es pico y
	# su vecino derecho es mayor
	# que eso, entonces la mitad derecha debe
	# tener un elemento pico
	else:
		return encuentra_PicoB(arr, (med + 1), alto, n)

# Un contenedor sobre recursivo
# función buscarPicoUtil()
def encuentraPicoA(arr, n):
	return encuentra_PicoB(arr, 0, n - 1, n)

# Datos
consumo = [5,254,3.1,101,0.9,145,272,199,909,299,104,334,102,5.1,1822,34.9,0.153,72,88,119,93,3.1,14,1,4]
consumo.sort() #ordenamiento
departamentos = ["MADRE DE DIOS", "AYACUCHO", "TUMBES","SAN MARTIN","APURIMAC","        UCAYALI","AMAZONAS","LAMBAYEQUE","        TACNA   ","LORETO","MOQUEGUA","PASCO","PUNO","AREQUIPA","LA LIBERTAD","ICA","PIURA    ","CAJAMARCA","CUSCO","ANCASH","CALLAO", "HUANUCO","JUNIN   ","HUANCAVELICA",  "LIMA   "]

# Muestra Valores picos
m = len(consumo)
p = encuentraPicoA(consumo, m) #retorna indice del valor pico
# 2016, la producción total de energía eléctrica a nivel nacional totalizó 51,768 GWh OSINERGMIN
# 2016, segundo sector con mayores emisiones de GEI reportada es Energía, con 58,132.54 GgCO2eq
# 2016 -> Emisiones GEI = (consumo * 58,132.54 )/ 51,768 GgCO2eq
print( "Producción de Energía Eléctrica\n")
print( "Cantidad de Departamentos: ",m)

#Graficar
from random import seed
import seaborn as sns
import matplotlib.pyplot as plt
seed(True)
#gráfico de barras
sns.set(style="whitegrid")
plt.figure(figsize=(29,8)) # Cambia tamaño grafico ancho - largo
plt.title("Producción de Energía Eléctrica en los Departamentos del Perú - Año 2021 - Mes Diciembre")   # Establece el título del gráfico
plt.xlabel("Departamentos del Perú")   # Establece el título del eje x
plt.ylabel("Consumo de Energía Eléctrica G(Wh)")   # Establece el título del eje y
x=["AM","AN","AP","AR","AY","CA","CAL","CU","HU","HUA","ICA","JUN","LAL","LAM","LIM","LO","MA","MO","PA","PI","PU","SA","TA","TU","UC"]
y=[5,254,3.1,101,0.9,145,272,199,909,299,104,334,102,5.1,1822,34.9,0.153,72,88,119,93,3.1,14,1,4]
ax=sns.barplot(x=x, y=y)

#solo línea
plt.plot(x,y)
plt.show()

print( "Resultados")
print( "----------\n")
import pandas as pd
print( "Valor Pico de Energía\n")
tabla = pd.DataFrame(data = [])
print( "N°\tConsumo (GWh)\tDepartamento    GEI aprox.(GgCO2eq)")
print("-----------------------------------------------------------")
print( 1, "\t   ", consumo[p], "\t", departamentos[p], "\t",round((consumo[p]* 58132.54)/ 51768,2))

print("-----------------------------------------------------------")
print("Total:     ", consumo[p],"                       ",round((consumo[p]* 58132.54)/ 51768,2))