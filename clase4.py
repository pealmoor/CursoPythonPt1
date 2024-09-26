#tipo de variable
name="Pedro"
caracter="c"
print(type(name))
print(type(caracter))

#comilla simple e indexación
name2='Pedro Molina'
print(name2[0])
print(name2[1])
print(name2[2])
print(name2[-1])
print(name2[-2])

#concatenación
name3="Alejandro"
name4="Ortiz"
print(name3+ " "+ name4)

#repetición
print(name3*3)

#longitud
print(len(name3))
print(len(name))

#minuscula y mayuscula
print(name2.lower())
print(name2.upper())
print(name2.strip())

"""""
Comandos más usados:

lower(): Convierte la cadena a minúsculas.
upper(): Convierte la cadena a mayúsculas.
strip(): Elimina espacios en blanco al inicio y al final.
split(): Divide la cadena en una lista de subcadenas.
join(): Une una lista de cadenas en una sola cadena.
replace(): Reemplaza una subcadena por otra.
startswith(): Verifica si la cadena comienza con una subcadena específica.
endswith(): Verifica si la cadena termina con una subcadena específica.
find(): Busca una subcadena y devuelve su posición.
count(): Cuenta las ocurrencias de una subcadena.
isalpha(): Verifica si todos los caracteres son alfabéticos.
isdigit(): Verifica si todos los caracteres son dígitos.
capitalize(): Convierte el primer carácter a mayúscula.
title(): Convierte la primera letra de cada palabra a mayúscula.
format(): Formatea la cadena con valores especificados.
"""""