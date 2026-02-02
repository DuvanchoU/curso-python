# Capítulo 3: Booleanos, Condicionales y Entrada de Usuario en Python.

# -----------------------------------------------------------------
# ENTRADA DE DATOS DEL USUARIO. IDENTIFICACIÓN DEL TIPO DE DATOS.
# -----------------------------------------------------------------

edad = input("Por favor, ingresa tu edad: ")  # Solicita al usuario que ingrese su edad
print("Has ingresado:", edad)  # Muestra la edad ingresada por el usuario

tipo_de_dato = type(edad)  # Obtiene el tipo de dato de la variable 'edad'
print("El tipo de dato de la variable 'edad' es:", tipo_de_dato)  # Muestra el tipo de dato

# -------------- BOOLEANOS , IF -------------------

verdadero = True  # Variable booleana con valor True
falso = False    # Variable booleana con valor False

if (verdadero == True):
    print("La variable 'verdadero' es True")  # Esta línea se ejecutará
    
if (falso == True):
    print("La variable 'falso' es True")  # Esta línea no se ejecutará
    
if (falso == False):
    print("La variable 'falso' es False")  # Esta línea se ejecutará
    
# ------------- OPERADORES DE COMPARACIÓN: ELIF, ELSE -----------------

edad = input("Por favor, dime tu edad: ")  # Solicita al usuario que ingrese su edad
edad = int(edad)  # Convierte la entrada de texto a un número entero

if edad < 0:
    print("Edad inválida") # Se ejecuta si la edad es menor a 0
elif edad >= 18:
    print("Eres mayor de edad, puedes pasar") # Se ejecuta si la edad es mayor o igual a 18
elif edad < 10:
    print("Eres un niño, no puedes pasar") # Se ejecuta si la edad es menor a 10
else:
    print("Eres menor de edad, no puedes pasar") # Se ejecuta si ninguna condición anterior se cumple
    
# ------------- OPERADORES LÓGICOS: AND, OR, NOT -----------------

edad = input("Por favor, dime tu edad: ")  # Solicita al usuario que ingrese su edad
edad = int(edad)  # Convierte la entrada de texto a un número entero

if(type(edad) == int): # Verifica si la variable 'edad' es de tipo entero
    if(edad > 120 or edad < 0):
        print("Edad inválida")  # Se ejecuta si la edad es mayor a 120 o menor a 0
    elif(edad >= 18 and edad < 40):
        print("Puedes entrar a la discoteca")  # Se ejecuta si la edad está entre 18 y 39
    elif(edad < 18 and edad > 15):
        print("Eres un adolescente, no puedes entrar")  # Se ejecuta si la edad está entre 16 y 17
    else:
        print("No ha cumplido ninguna condición")  # Se ejecuta si ninguna condición anterior se cumple
else:
    print("Por favor, ingresa un número válido")  # Se ejecuta si la entrada no es un número entero
    
# ------------- NOT -----------------

if(not(edad <= 18)):
    print("Eres mayor de edad, puedes pasar")  # Se ejecuta si la edad no es menor a 18
    
# EJERCICIO: Comprobar si el usuario introduce un número y no texto, validar si es par o impar. Notificarselo al usuario.
# PISTAS: isnumeric(), num%2 = 0

#SOLUCIÓN:
numero = input("Por favor, ingresa un número: ")  # Solicita al usuario que ingrese un número
if(not(numero.isnumeric())):
    print("Datos inválidos. Debe ser un número")  # Se ejecuta si la entrada no es un número
else:
    numero = int(numero)  # Convierte la entrada de texto a un número entero
    if(numero % 2 == 0):
        print("El número", numero, "es par")  # Se ejecuta si el número es par
    else:
        print("El número", numero, "es impar")  # Se ejecuta si el número es impar