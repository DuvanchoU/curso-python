# Capítulo 6: Listas en Python

# ------------ APARTADO 1: REPASO DE CONCEPTOS BÁSICOS SOBRE LISTAS ------------

numeros = [1, 2, 3, 4, 5]  # Las posiciones inician en 0
print("Lista de números:", numeros)  # Muestra la lista completa
primeraPosicion = numeros[0]  # Muestra el primer número de la lista

longitudLista = len(numeros)  # Muestra la longitud de la lista
print(f"Primer número de la lista: {primeraPosicion}")  # Muestra el primer número de la lista
print(f"Longitud de la lista: {longitudLista}")  # Muestra la longitud de la lista

for num in numeros:  # Bucle que recorre cada número de la lista
    print(num)  # Imprime el número actual
    
# -------------- APARTADO 2: INDICES NEGATIVOS Y SUBLISTAS --------------

lista = ["El", "rey", "de", "la", "selva"]
print("Lista original:", lista)  # Muestra la lista completa
ultimaPosicion = lista[-1]  # Accede al último elemento de la lista
print(f"Último elemento de la lista: {ultimaPosicion}")  # Muestra el último elemento de la lista
penUltimaPosicion = lista[-2]  # Accede al penúltimo elemento de la lista
print(f"Penúltimo elemento de la lista: {penUltimaPosicion}")  # Muestra el penúltimo elemento de la lista

sublista = lista[1:4]  # Crea una sublista desde la posición 1 hasta la 3
print("Sublista (posiciones 1 a 3):", sublista)  # Muestra la sublista
sublista = lista[:4]  # Crea una sublista desde el inicio hasta la posición 
print("Sublista (inicio a posición 4):", sublista)  # Muestra la sublista
sublista = lista[2:]  # Crea una sublista desde la posición 2 hasta el final
print("Sublista (posición 2 a final):", sublista)  # Muestra

sublista = lista[-4:-1] # Crea una sublista usando índices negativos
print("Sublista (índices negativos -4 a -1):", sublista)  # Muestra la sublista

# -------------- APARTADO 3: COMPROBAR SI UNA LISTA CONTIENE O NO UN ELEMENTO --------------

lista = ["manzana", "banano", "naranja", "pera", "uva"]
palabra = "naranja"
palabraDos = "kiwi" 

if palabra in lista:  # Verifica si la palabra está en la lista
    print(f"{palabra} está en la lista.")  # Muestra que la palabra está en la lista

if palabraDos not in lista:  # Verifica si la palabra no está en la lista
    print(f"{palabraDos} no está en la lista.")  # Muestra que la palabra no está en la lista
    
# -------------- APARTADO 4: MODIFICAR ELEMENTOS A UNA LISTA --------------

lenguajes = ["Python", "Java", "C", "JavaScript", "Php", "HTML"]
print(lenguajes)  # Muestra la lista original
lenguajes[1] = "Ruby"  # Modifica el elemento en la posición 1
print(lenguajes)  # Muestra la lista después de la modificación
lenguajes[2] = lenguajes[2] + "++" # Modifica el elemento en la posición 2 concatenando "++"
print(lenguajes)  # Muestra la lista después de la modificación

lenguajes[2:4] = ["C#", "Go"]  # Modifica los elementos en las posiciones 2 y 3
print(lenguajes)  # Muestra la lista después de la modificación

lenguajes[4:5] = ["Swift", "Kotlin", "Rust"]  # Modifica el elemento en la posición 4 con múltiples elementos
print(lenguajes)  # Muestra la lista después de la modificación

# -------------- APARTADO 5: AGREGAR ELEMENTOS A UNA LISTA --------------

animales = ["perro", "gato", "pez", "conejo", "hamster"]
print(animales)  # Muestra la lista original

animales.insert(2, "tortuga")  # Inserta "tortuga" en la posición 2 
print(animales)  # Muestra la lista después de la inserción

animales.append("loro")  # Agrega "loro" al final de la lista
print(animales)  # Muestra la lista después de agregar al final

animalesDos = ["serpiente", "iguana", "león"]
animales.extend(animalesDos)  # Extiende la lista con otra lista
print(animales)  # Muestra la lista después de extenderla
print(animalesDos)  # Muestra la segunda lista original

animalesDos.extend(animales)  # Extiende la segunda lista con la primera lista
print(animalesDos)  # Muestra la segunda lista después de extenderla

# -------------- APARTADO 6: ELIMINAR ELEMENTOS DE UNA LISTA --------------

colores = ["rojo", "azul", "verde", "amarillo", "morado", "naranja"]
print(colores)  # Muestra la lista original

colores.pop()  # Elimina el último elemento de la lista
print(colores)  # Muestra la lista después de eliminar el último elemento

elementoEliminado = colores.pop(2)  # Elimina el elemento en la posición 2
print(f"Elemento eliminado: {elementoEliminado}")  # Muestra el elemento eliminado
print(colores)  # Muestra la lista después de eliminar el elemento en la posición 2

colores.remove("azul")  # Elimina el elemento "azul" de la lista
print(colores)  # Muestra la lista después de eliminar el elemento "azul"

del colores[0] # Elimina el elemento en la posición 0
print(colores)  # Muestra la lista después de eliminar el elemento en la posición 0

indice = colores.index("morado")  # Obtiene el índice del elemento "morado"
print(f"Índice de 'morado': {indice}")  # Muestra el índice del elemento "morado"

# --------------------- EJERCICIO -------------------------------

# Disponemos de un texto en el que queremos buscar palabras clave.
# El programa debe pedir al usuario palabras clave (como máximo 5).
# Las palabras se deben introducir una a una.
# El usuario puede terminar la introducción de palabras escribiendo:
# "fin".

# Si el usuario introduce números, cadenas vacías u otros valores no válidos,
# estos NO deben añadirse a la lista de palabras clave.
# Una vez obtenidas las palabras clave, el programa debe analizar el texto
# y contar cuántas veces aparece cada palabra.
# Debemos guardar los resultados en dos listas:
# - Una lista con las palabras clave.
# - Otra lista con el número de apariciones de cada palabra.

# Por ejemplo, si las palabras clave son:
# ["ordenador", "portátil"]
# y aparecen 5 y 7 veces respectivamente en el texto, el resultado será:
# keywords = ["ordenador", "portátil"]
# occurrences = [5, 7]

# Cada posición de la lista occurrences debe corresponder con la misma
# posición de la palabra en la lista keywords.

# Pista: Podemos pasar de una cadena de texto a una lista de palabras mediante
# el método texto.split(). Por ejemplo:

# texto = "hola que tal"
# print(texto.split())
# Resultado: ['hola', 'que', 'tal']

# SOLUCIÓN:

texto = """
Seguramente hayas notado que tu productividad ha bajado desde que trabajas desde casa.
Es muy importante que logremos teletrabajar efectivamente y de manera autorregulada.
Esto se traduce en finalizar antes nuestras tareas y evitar jornadas laborales interminables.
El primer consejo y uno de los más importantes ya te lo he dado en el apartado anterior.
Tenemos que construir un espacio de trabajo en el que nos sintamos cómodos y dispongamos de todas las herramientas necesarias para teletrabajar.
En la medida de lo posible, es importante teletrabajar siempre en el mismo lugar.
De esta forma, nuestro cerebro asocia el sitio con la acción de trabajar y nos hará estar más focalizados en nuestras tareas.
"""
keywords = [] # Lista para almacenar las palabras clave introducidas por el usuario
ocurrencias = [] # Lista para almacenar el número de apariciones de cada palabra clave en el texto

for i in range(5): # Bucle para pedir al usuario que introduzca hasta 5 palabras clave
    keyword = input("Introduce una palabra clave (o 'fin' para terminar): ").strip().lower() 

    if keyword == "fin": # Si el usuario introduce "fin", se termina la introducción de palabras clave
        break

    if keyword == "" or keyword.isnumeric(): # Si el usuario introduce una cadena vacía o un número, se ignora esa entrada y se continúa con la siguiente iteración del bucle
        continue

    keywords.append(keyword) # Si la entrada es válida, se añade a la lista de palabras clave

print(keywords)

posicion = 0

while True:
    if posicion >= len(keywords): # Si la posición actual es mayor o igual que la longitud de la lista de palabras clave, se termina el bucle
        break

    if keywords[posicion] == "" or keywords[posicion].isnumeric(): # Si la palabra clave en la posición actual es una cadena vacía o un número, se elimina esa palabra clave de la lista
        keywords.pop(posicion)
    else:
        posicion += 1 # Si la palabra clave es válida, se pasa a la siguiente posición

print("Lista de keywords corregida:", keywords)

texto_limpio = texto.lower() # Convertimos el texto a minúsculas para que la búsqueda de palabras clave sea insensible a mayúsculas
texto_limpio = texto_limpio.replace(",", "") # Eliminamos las comas del texto para que no afecten a la búsqueda de palabras clave
texto_limpio = texto_limpio.replace(".", "") # Eliminamos los puntos del texto para que no afecten a la búsqueda de palabras clave
texto_limpio = texto_limpio.replace("\n", " ") # Reemplazamos los saltos de línea por espacios para que el texto se trate como una sola cadena continua

palabras_texto = texto_limpio.split() # Convertimos el texto limpio en una lista de palabras utilizando el método split()

for _ in range(len(keywords)): # Inicializamos la lista de ocurrencias con ceros para cada palabra clave
    ocurrencias.append(0)

for palabra in palabras_texto: # Bucle para contar las apariciones de cada palabra clave en el texto
    for i in range(len(keywords)): # Bucle para comparar cada palabra del texto con cada palabra clave
        if palabra == keywords[i]: # Si la palabra del texto coincide con la palabra clave en la posición i, se incrementa el contador de ocurrencias para esa palabra clave
            ocurrencias[i] += 1

print("Ocurrencias:", ocurrencias)
        