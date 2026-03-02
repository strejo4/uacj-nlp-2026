# Tarea 2 - Expresiones Regulares en Python
# Nombre: Sergio Trejo
# Matrícula: 261539
# Materia: Procesamiento de Lenguaje Natural
# observar el funcionamiento básico de las expresiones regulares en Python.

# -------------------------------------------------
# En Python, las expresiones regulares están soportadas por el módulo re
# -------------------------------------------------

import re

# -------------------------------------------------
# Los caracteres ordinarios son las expresiones regulares más sencillas. Coinciden exactamente consigo mismas y no tienen un significado especial en su sintaxis de expresión regular.
# Ejemplos: "A", "a", "X", "5"
# En este ejemplo, buscamos la palabra "Cookie" en la cadena "Cookie". Dado que ambas son idénticas, se produce una coincidencia.
# -------------------------------------------------

pattern = r"Cookie" 
sequence = "Cookie" 
if re.match(pattern, sequence): 
    print("Match!")
else: print("Not a match!")

# -------------------------------------------------
# Caracteres especiales
# Los caracteres especiales son caracteres que no coinciden por sí mismos, pero que tienen un significado especial cuando se utilizan en una expresión regular
# Se puede pensar en ellos como metacaracteres reservados que denotan otra cosa y no lo que parecen
# Los ejemplos siguientes utilizan dos funciones: search() y group(). 
# Con la función de búsqueda, recorres la cadena/secuencia dada, buscando la primera posición en la que la expresión regular produzca una coincidencia.
# La función grupo devuelve la cadena coincidente con la re. Verás estas dos funciones con más detalle más adelante.
# -------------------------------------------------
# . - Coincide con cualquier caracter excepto salto de línea
# -------------------------------------------------
resultado = re.search(r'Co.k.e', 'Cookie').group()
print(resultado)

# -------------------------------------------------
# ^ - Coincide con el inicio de la cadena
# -------------------------------------------------
resultado = re.search(r'^Eat', "Eat cake!").group()
print(resultado)

resultado = re.search(r'^eat', "Let's eat cake!")
print(resultado)

# -------------------------------------------------
# $ - Coincide con el final de la cadena
# -------------------------------------------------
resultado = re.search(r'cake$', "Cake! Let's eat cake").group()
print(resultado)

resultado = re.search(r'cake$', "Let's get some cake on our way home!")
print(resultado)

# -------------------------------------------------
# [abc] - Conjuntos de caracteres
# -------------------------------------------------
resultado = re.search(r'[0-6]', 'Number: 5').group()
print(resultado)

resultado = re.search(r'Number: [^5]', 'Number: 0').group()
print(resultado)

resultado = re.search(r'Number: [^5]', 'Number: 5')
print(resultado)

# -------------------------------------------------
# Barras invertidas y escapes
# -------------------------------------------------
resultado = re.search(r'Not a\sregular character', 'Not a regular character').group()
print(resultado)

resultado = re.search(r'Just a \regular character', 'Just a \\regular character')
print(resultado)

resultado = re.search(r'Just a \\sregular character', 'Just a \\sregular character').group()
print(resultado)

# -------------------------------------------------
# Secuencias especiales \w y \W
# -------------------------------------------------
print("Lowercase w:", re.search(r'Co\wk\we', 'Cookie').group())
print("Uppercase W:", re.search(r'C\Wke', 'C@ke').group())

resultado = re.search(r'Co\Wk\We', 'Cookie')
print("Uppercase W no coincide:", resultado)

# ----------------------------------------------------------------
# \s - espacio en blanco, \S - no espacio
# ----------------------------------------------------------------
print("Lowercase s:", re.search(r'Eat\scake', 'Eat cake').group())
print("Uppercase S:", re.search(r'cook\Se', "Let's eat cookie").group())

# -------------------------------------------------
# \d y \D - dígitos
# -------------------------------------------------
print("How many cookies do you want? ", re.search(r'\d+', '100 cookies').group())

# -------------------------------------------------
# Ejemplo de \t (tab) y \b (borde de palabra)
# -------------------------------------------------
print("\\t (TAB) example:", re.search(r'Eat\tcake', 'Eat\tcake').group())
print("\\b match gives: ", re.search(r'\b[A-E]ookie', 'Cookie').group())

# -----------------------------------------------
# Repeticiones: +, *, ?, {x}, {x,y}
# -----------------------------------------------
print(re.search(r'Co+kie', 'Cooookie').group())
print(re.search(r'Ca*o*kie', 'Cookie').group())
print(re.search(r'Colou?r', 'Color').group())

# {x,y} ejemplo
resultado = re.search(r'\d{9,10}', '0987654321').group()
print(resultado)

# -------------------------------------------------
# Agrupación de patrones
# -------------------------------------------------
statement = 'Please contact us at: support@datacamp.com'
match = re.search(r'([\w\.-]+)@([\w\.-]+)', statement)
if match:
    print("Email address:", match.group())
    print("Username:", match.group(1))
    print("Host:", match.group(2))

# -------------------------------------------------
# Grupos con nombre
# -------------------------------------------------
match_named = re.search(r'(?P<email>(?P<username>[\w\.-]+)@(?P<host>[\w\.-]+))', statement)
if match_named:
    print("Email address:", match_named.group('email'))
    print("Username:", match_named.group('username'))
    print("Host:", match_named.group('host'))

# -------------------------------------------------
# Coincidencias codiciosas vs no codiciosas
# -------------------------------------------------
heading = r'<h1>TITLE</h1>'
print(re.match(r'<.*>', heading).group())
print(re.match(r'<.*?>', heading).group())
