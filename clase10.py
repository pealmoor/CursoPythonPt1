numbers={1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])

information={"nombre":"Pedro", 
             "apellido":"Molina", 
             "cedula":"1090516812"}


del information["cedula"]
print (information)
claves=information.keys()
print(claves)
#print(type(claves))


values=information.values()
print(values)

contacts={"Pedro": { 
          "apellido":"Molina", 
          "cedula":"1090516812"},
          "Diego":{ "apellido":"Ortiz", 
          "cedula":"1090516813"}}

print(contacts["Pedro"])