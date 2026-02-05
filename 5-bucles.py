# Capítulo 5: Bucles en Python

# -------------------------------
# ---------- PARTE 1 ------------
# INTRODUCCIÓN A LAS LISTAS
# -------------------------------

numeros = [1, 2, 3, 4, 5]  # Las posiciones inician en 0
print("Lista de números:", numeros)  # Muestra la lista completa
print("Primer número de la lista:", numeros[0])  # Muestra el primer número de la lista
print("Tercer número de la lista:", numeros[2])  # Muestra el tercer número de la lista

print("Longitud de la lista:", len(numeros))  # Muestra la longitud de la lista

textos = ["Hola", "Mundo", "Python"]  # Lista de textos
print("Lista de textos:", textos)  # Muestra la lista de textos
print("Segundo texto de la lista:", textos[1])  # Muestra el segundo texto de la lista

print("Longitud de la lista de textos:", len(textos))  # Muestra la longitud de la lista de textos

# -------------- BUCLES FOR -------------------

for x in range(5):  # Bucle que se repite 5 veces
    print(x)  # Mensaje que se muestra en cada iteración
print("Hemos terminado el bucle.")  # Mensaje al finalizar el bucle

for x in range(2, 8):  # Bucle que se repite desde 2 hasta 7
    print(x)  # Mensaje que se muestra en cada iteración
    
for x in range(1, 10, 2):  # Bucle que se repite desde 1 hasta 9 con paso de 2
    print(x)  # Mensaje que se muestra en cada iteración

# --- MINI EJEMPLO, IMPRIMIR SOLO LAS VOCALES DE UNA PALABRA ---

palabra = "programacion"  # Palabra de ejemplo
for letra in palabra:  # Bucle que recorre cada letra de la palabra
    if (letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'): # Verifica si la letra es una vocal
        print(letra)  # Imprime la vocal encontrada
    else:
        print("No es vocal")  # Indica que no es una vocal

# ------ MINI EJEMPLO, RECORRER UNA LISTA Y MODIFICAR UNA VARIABLE TEMPORAL ------

numeros = [10, 20, 30, 40, 50]  # Lista de números
for numero in numeros:  # Bucle que recorre cada número de la lista
    print(numero)  # Imprime el número actual
    numero += 5  # Suma 5 al número actual
    print("Número después de sumar 5:", numero)  # Imprime el número después de la suma

# ------ MINI EJEMPLO, SUMAR 5 A CADA ELEMENTO DE LA LISTA ------

for indice in range(len(numeros)):  # Bucle que recorre los índices de la lista
    numeros[indice] += 5  # Suma 5 al número en la posición actual
print("Lista de números después de sumar 5 a cada uno:", numeros)  # Muestra la lista modificada

# -------------------- BUCLES WHILE -----------------------

contador = 0  # Inicializa el contador en 0
while(contador < 10):  # Bucle que se repite mientras el contador sea menor que 10
    print("Contador:", contador)  # Muestra el valor actual del contador
    contador += 1  # Incrementa el contador en 1

letraEncontrada = False  # Variable para indicar si se encontró la letra 'a'
letra = "a"  # Inicializa la letra en 'a'
frase = "En este momento estoy buscando la letra a."  # Frase de ejemplo
indice = 0  # Inicializa el índice en 0

# SE ASUME QUE LA LETRA 'a' ESTÁ EN LA FRASE PARA EVITAR BUCLE INFINITO
while(not(letraEncontrada)):
    if(frase[indice] == letra):  # Verifica si la letra actual es 'a'
        letraEncontrada = True  # Cambia la variable a True si se encuentra la letra
        print(f"Ya hemos encontrado la letra {letra} en la posición {indice}!")  # Muestra la posición donde se encontró la letra
    else:
        indice += 1  # Incrementa el índice para revisar la siguiente letra
    
# -------------------------------
# ---- INICIO DE LA PARTE 2 -----
# -------------------------------

# --------------------- BREAK ------------------------
frase = "En este momento estoy buscando la letra y." 
letra = "y"

indice = 0
for caracter in frase:  # Bucle que recorre cada carácter de la frase
    if(caracter == letra):  # Verifica si el carácter actual es 'y'
        print(f"Hemos encontrado la letra {letra} en la posición {indice}!")  # Muestra que se encontró la letra
        print(caracter)
        break  # Sale del bucle al encontrar la letra
    else:
        print("No es la letra que buscamos.")  # Indica que no es la letra buscada
        
# --------------------- CONTINUE ------------------------
frase = "Hola Duvancho"
letra = "a"
count = 0

for caracter in frase:  # Bucle que recorre cada carácter de la frase
    if (caracter == letra):  # Verifica si el carácter actual es 'a'
        count += 1  # Incrementa el contador si se encuentra la letra
        print(f"Letra {letra} encontrada {count} veces.")  # Muestra cuántas veces se ha encontrado la letra
        continue  # Continúa con la siguiente iteración del bucle
    print("No es la letra que buscamos.")  # Indica que no es la letra buscada
    
# --------------------- PASS ------------------------
lista = [10, 20, 30, 40, 50]
for duvan in lista:  # Bucle que recorre cada número de la lista
    if duvan == 30:  # Si el número es 30, no hace nada (pass)
        pass  # No realiza ninguna acción
    else:
        print(duvan)  # Imprime el número si no es 30

# --------------------- ELSE ------------------------
frase = "Buscando la letra z en esta frase."
count = 0
for caracter in frase:  # Bucle que recorre cada carácter de la frase
    count += 1  # Incrementa el contador
    if(caracter == 'z'):  # Verifica si el carácter actual es 'z'
        break  # Sale del bucle al encontrar la letra 
else:
    print(f"La letra z no se encontró en la frase después de revisar {count} caracteres.")  # Muestra que no se encontró la letra

# EJERCICIO:
# Crear un programa que permita al usuario adivinar un número entre 0 y 10.
# El programa debe generar o definir un número a adivinar.
# Luego debe pedir al usuario que ingrese un número.
# Finalmente, debe indicar si el número ingresado es correcto
# o si el número a adivinar es mayor o menor que el número introducido por el usuario.

numeroCorrecto = 7 # Número que el usuario debe adivinar

def pedirYComprobar(numeroAdivinar):
    """
    Función que pide un número al usuario y comprueba
    si es igual, mayor o menor que el número a adivinar.
    Retorna True si acierta, False si no.
    """

    # Se pide el dato al usuario (siempre llega como texto)
    dato = input("Adivina el número (entre 0 y 10): ")

    # Se valida que el usuario haya ingresado un número
    if not dato.isnumeric():
        print("Error: debes ingresar un número válido.")
        return False

    # Se convierte el texto a número entero
    numero = int(dato)

    # Se compara el número ingresado con el número a adivinar
    if numero == numeroAdivinar:
        print("¡Eres un crack, has acertado!")
        return True

    elif numero > numeroAdivinar:
        print("Casi, pero el número debe ser más pequeño.")
        return False

    else:
        print("Casi, pero el número debe ser más grande.")
        return False

# Bucle que se repite hasta que el usuario acierte el número
while True:
    # Si la función retorna True, se termina el juego
    if pedirYComprobar(numeroCorrecto):
        break