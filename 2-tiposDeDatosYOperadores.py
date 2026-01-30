# Capitulo 2: Tipos de Datos y Operadores Aritméticos en Python.

# -------------------------------------
# VARIABLES Y TIPOS DE DATOS NUMÉRICOS
# -------------------------------------

# Se declara una variable de tipo entero
numero_entero = 10          
print(numero_entero)  # Muestra el valor del número entero

# Se declara una variable de tipo decimal (float)
numero_decimal = 3.14      
print(numero_decimal)  # Muestra el valor del número decimal

# Se suma 4 al valor actual de numero_entero
numero_entero = numero_entero + 4   
print(numero_entero)  # Muestra el nuevo valor de numero_entero

# Se suma un entero con un decimal (el resultado será decimal)
numero = numero_entero + numero_decimal
print(numero)  # Muestra el resultado de la suma

# Operador de asignación abreviada (suma 4 al valor actual)
numero_entero += 4  
print(numero_entero)  # Muestra el nuevo valor de numero_entero

# Se declara una variable numérica
variable_numerica = 20
# Se resta 10 al valor de la variable
variable_numerica = variable_numerica - 10
print(variable_numerica)  # Muestra el resultado de la resta

# Se declara otra variable
variable = 10
# Se divide la variable entre variable_numerica
variable = variable / variable_numerica
print(variable)  # Muestra el resultado de la división

# Se realiza una operación combinada (primero la división, luego la suma)
numero = 2 / 2 + 3
print(numero)  # Muestra el resultado de la operación

# Multiplicación entre dos números enteros
multiplicacion = 2 * 3
print(multiplicacion)  # Muestra el resultado de la multiplicación

# Multiplicación entre un entero y un decimal
multiplicacion = numero_entero * numero_decimal
print(multiplicacion)  # Muestra el resultado

# Potencia (2 elevado a la 3)
potencia = 2 ** 3

# Módulo (residuo de la división)
modulo = 11 % 2

print(potencia)  # Muestra el resultado de la potencia
print(modulo)    # Muestra el residuo de la división

# -------------------------------
# TIPOS DE DATOS: TEXTO (STRINGS)
# -------------------------------

# Texto usando comillas dobles
texto = "Hola Soy Duvan!"

# Texto usando comillas dobles con comillas simples dentro
text = "Estoy 'aprendiendo' Python."

# Texto usando comillas simples con comillas dobles dentro
textt = 'El lenguaje de programación Python es "genial".'

# Texto simple
txt = 'Sorprendente!'

print(texto)  # Muestra el texto
print(text)   # Muestra el texto
print(textt)  # Muestra el texto
print(txt)    # Muestra el texto

# Texto de varias líneas usando triple comilla
texto_con_formato = """Este es un texto
con varias líneas."""

print(texto_con_formato)  # Muestra el texto en varias líneas