# Capítulo 4: Funciones en Python.

# -------------------------------
# DEFINICIÓN Y USO DE FUNCIONES.
# -------------------------------

def saludar():
    """Función que saluda al usuario."""
    print("¡Hola! Bienvenido a nuestro programa.")  # Mensaje de saludo
    
saludar()  # Llamada a la función para ejecutar el saludo

# -------------- FUNCIONES CON ARGUMENTOS -------------------
def saludarDos(nombre):
    """Función que saluda al usuario por su nombre."""
    print(f"¡Hola, {nombre}! Bienvenido a nuestro programa.")  # Mensaje de saludo personalizado
    
saludarDos("Duvan")  # Llamada a la función con el nombre "Duvan"
saludarDos("Andrea")    # Llamada a la función con el nombre "Andrea"

# -------------- FUNCIONES CON VALOR DE RETORNO -------------------
# 1. OPCIÓN
def sumar(a, b): 
    resultado = a + b  # Suma los dos números
    return resultado  # Retorna el resultado de la suma

valor = sumar(5, 3)  # Llamada a la función sumar con los valores 5 y 3
print("El resultado de la suma es:", valor)  # Muestra el resultado de la suma

valor = sumar(10, 20)  # Llamada a la función sumar con los valores 10 y 20
print("El resultado de la suma es:", valor)  # Muestra el resultado de la suma

# 2. OPCIÓN
def sumaDos(a, b):
    return a + b  # Retorna la suma de los dos números

#--------------------------------------------------------------------------------
valor = sumaDos(5, 3)  # Llamada a la función sumaDos con los valores 5 y 3
print("El resultado de la suma es:", valor)  # Muestra el resultado de la suma

valor = sumaDos(10, 20)  # Llamada a la función sumaDos con los valores 10 y 20
print("El resultado de la suma es:", valor)  # Muestra el resultado de la suma

def sonIguales (num1, num2):
    """Función que verifica si dos números son iguales."""
    return num1 == num2  # Retorna True si son iguales, False si no lo son

verdad = sonIguales(5, 5)  # Llamada a la función sonIguales con los valores 5 y 5
if(verdad):
    print("Los números son iguales") 
    
print("¿Son iguales los números?", verdad)  # Muestra si los números son iguales

falso = sonIguales(5, 3)  # Llamada a la función sonIguales con los valores 5 y 3
if(falso):
    print("Los números son iguales")
    
print("¿Son iguales los números?", falso)  # Muestra si los números son iguales

# -------------- FUNCIONES CON ARGUMENTOS CON VALOR POR DEFECTO -------------------

def saludarPorDefecto(nombre="Usuario"):
    """Función que saluda al usuario, con un nombre por defecto."""
    print(f"¡Hola, {nombre}! Bienvenido a nuestro programa.")  # Mensaje de saludo personalizado

saludarPorDefecto()  # Llamada a la función sin argumentos, usa el valor por defecto
saludarPorDefecto("Andres")  # Llamada a la función con el nombre "Andres"

# -------------- FUNCIONES QUE RETORNAN VARIOS VALORES -------------------

# 1. OPCIÓN
def sumaYResta(a, b):
    """Función que retorna la suma y la resta de dos números."""
    suma = a + b  # Calcula la suma
    resta = a - b  # Calcula la resta
    return suma, resta  # Retorna ambos resultados

# 2. OPCIÓN
def sumaYRestaDos(a, b):
    """Función que retorna la suma y la resta de dos números."""
    return a + b, a - b  # Retorna la suma y la resta directamente

# ---------------------------------------------------------------------------------
resultado1, resultado2 = sumaYResta(10, 5)  # Llamada a la función sumaYResta con los valores 10 y 5
print("Suma:", resultado1)  # Muestra el resultado de la suma
print("Resta:", resultado2)  # Muestra el resultado de la resta

# EJERCICIO 1:
# Crear una función llamada maximo() que reciba dos números como parámetros.
# La función debe validar que ambos argumentos sean de tipo int o float.
# Si alguno de los valores no es numérico, debe mostrar un mensaje de error y retornar False.
# Si ambos valores son válidos, la función debe determinar cuál número es mayor y retornarlo.

# SOLUCIÓN:
def maximo(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)): # Verifica si ambos argumentos son numéricos
        if num1 == num2:
            print("Los números son iguales") 
            return num1 # Retorna cualquiera de los dos números si son iguales
        elif num1 > num2: # Compara los dos números
            return num1 # Retorna el número mayor
        else:   
            return num2 # Retorna el número mayor
    else:
        print("Error: Ambos argumentos deben ser numéricos (int o float).")
        return False
    
num = maximo(10, 20)  # Llamada a la función maximo con los valores 10 y 20
if num != False:
    print("El número máximo es:", num)  # Muestra el número máximo retornado por la función
    
num = maximo(10, "Verde")  # Llamada a la función maximo con los valores 10 y "Verde"
if num != False:
    print("El número máximo es:", num)  # Muestra el número máximo retornado por la función
    
# EJERCICIO 2:
# Crear una mini calculadora que solicite al usuario una operación y dos números.
# Las operaciones permitidas son: suma, resta y potencia.
# El programa debe validar que la operación ingresada sea válida.
# Si la operación no es válida, debe mostrar un mensaje de error.
# Si la operación es correcta, debe realizar el cálculo y mostrar el resultado.

# SOLUCIÓN:

def calculadora():
    operacion = input("Por favor, ingresa la operación que deseas realizar (suma, resta, potencia): ")  # Solicita la operación al usuario
    if(not(operacion in ["suma", "resta", "potencia"])):
        print("Error: Operación no válida.")  # Mensaje de error para operación inválida
        return None
    num1 = float(input("Ingresa el primer número: "))  # Solicita el primer número
    num2 = float(input("Ingresa el segundo número: "))  # Solicita el segundo número
    
    if(operacion == "suma"):
        print(num1 + num2)  # Retorna la suma
    elif(operacion == "resta"):
        print(num1 - num2)  # Retorna la resta
    elif(operacion == "potencia"):
        print(num1 ** num2)  # Retorna la potencia
    else:
        print("Error: Operación no válida.")  # Mensaje de error para operación inválida
        return None
    
calculadora ()  # Llamada a la función calculadora
calculadora ()  # Llamada a la función calculadora
