to_do=["Dirigirnos al hotel",
       "Ir a almorzar",
       "Visitar un museo",
       "Volver al hotel"]
print(to_do)
numbers=[1,2,3,"cuatro"]
print(numbers)
print(type(numbers))

mix=[1,2,3,"cuatro", True, [1,2,3,"Siete"]]
print(mix)
print(len(mix))

print("La primera posicion es: " ,mix[0] )
print("La segunda posicion es: " ,mix[1] )
print("La pultima posicion es: " ,mix[-1] )

print(mix[0:2])
print(mix[2:])

#Añadir un nuevo valor
mix.append(False)
print(mix)
mix.append(["a","b","c"])
print(mix)

#Insertar un dato
mix.insert(1,["c","d"])
print(mix)
print(mix.index(["c","d"]))

#Mayor Menor

numbers=[1,2,3,100,300,2,3,4555]
print("Mayor", max(numbers))
print("Menor", min(numbers))

#Eliminar
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)
""""
Se elimina la lista:

del numbers
print(numbers)

"""