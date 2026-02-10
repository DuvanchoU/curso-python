# Capítulo 7: Cadenas de caracteres o Strings
# En este capítulo se trabajan conceptos básicos de manejo de textos en Python

# ------- APARTADO 1: REPASO DE CONCEPTOS BÁSICOS ------

texto = "Hola ¿Qué tal?" # Se asigna un string usando comillas dobles
print(texto)                          

texto = 'Hola ¿Qué tal?' # Se asigna un string usando comillas simples
print(texto)                       

stringConFormato = """     # Se crea un string multilínea (con saltos de línea)
========= TEXTO CON FORMATO ========
EL texto formateado:
    1.- Poner saltos de linea.
    2.- Poner sangrias.
y mostrarlo así por pantalla.
"""
print(stringConFormato)          

valorEntero = 5      # Se crea una variable de tipo entero
valorDecimal = 3.20  # Se crea una variable de tipo decimal (float)
valorBooleano = True # Se crea una variable de tipo booleano

print("Tipos de datos originales: ")  
print(type(valorEntero))              # Se muestra el tipo de dato de valorEntero
print(type(valorDecimal))             # Se muestra el tipo de dato de valorDecimal
print(type(valorBooleano))            # Se muestra el tipo de dato de valorBooleano

valorEntero = str(valorEntero)        # Se convierte el entero a string
valorDecimal = str(valorDecimal)      # Se convierte el decimal a string
valorBooleano = str(valorBooleano)    # Se convierte el booleano a string

print("Tipos de datos modificados: ") 
print(type(valorEntero))              # Se muestra el nuevo tipo de valorEntero
print(type(valorDecimal))             # Se muestra el nuevo tipo de valorDecimal
print(type(valorBooleano))            # Se muestra el nuevo tipo de valorBooleano

texto = "0123456789"                  # Se asigna un string con números
print("La longitud del texto es: ")   
print(len(texto))                     # Se imprime la cantidad de caracteres del string

texto1 = "01234"                      # Primer fragmento de texto
texto2 = "56789"                      # Segundo fragmento de texto

texto3 = "Los valores son: " + texto1 + texto2   # Se concatenan varios strings
print(texto3)                        

# ------- APARTADO 2: LOS STRINGS SON LISTAS -----------

texto = "0123456789"         # Se define nuevamente el string

primerCaracter = texto[0]    # Se obtiene el primer carácter del string
subString = texto[1:5]       # Se obtiene un sub-string desde la posición 1 hasta la 4

print("El texto original es: " + texto)         # Se imprime el texto completo
print("El primer valor es: " + primerCaracter)  # Se imprime el primer carácter
print("El subString es: " + subString)          # Se imprime el sub-string
print("El último caracter es: " + texto[-1])    # Se imprime el último carácter del string

print("Iteración: ")         

for num in texto:    # Se recorre cada carácter del string
    print("El número actual es: " + num)  # Se imprime el carácter actual

# ---------------- EJERCICIO (mini): -----------------------
# Dado un string compuesto únicamente por dígitos (números enteros),
# se debe recorrer cada carácter, convertirlo a entero y
# calcular la suma total de todos sus valores.
# Finalmente, mostrar el resultado por pantalla.

numeros = "3461264836565"    # String que contiene solo números
total = 0                    # Variable acumuladora para la suma

for numero in numeros:       # Se recorre cada carácter del string
    total += int(numero)     # Se convierte el carácter a entero y se suma
else:                                
    print("El valor total: " + str(total))  # Se muestra la suma total

# -------- APARTADO 3: FORMAT STRINGS -----------------

cantidad = 8                       
precio = 2500                         

# Forma 1: concatenando con str()
print("Has comprado " + str(cantidad) +          # Se concatena la cantidad convertida a string
      " botellas de agua. Cada botella vale $"   
      + str(precio) +                             # Se concatena el precio
      " COP. En total son $"                
      + str(cantidad * precio) + " COP")          # Se calcula y concatena el total

# Forma 2: usando format()
texto = "Has comprado {} botellas de agua. Cada botella vale ${} COP. En total son ${} COP"  # Plantilla de texto
print(texto.format(cantidad, precio, cantidad * precio))  # Se reemplazan los valores con format()

# Forma 3: usando f-string (la más recomendada hoy)
print(f"Has comprado {cantidad} botellas de agua. Cada botella vale ${precio} COP. En total son ${cantidad * precio} COP")
# Se usan variables directamente dentro del texto con f-string