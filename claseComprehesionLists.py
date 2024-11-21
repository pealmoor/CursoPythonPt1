squares=[x**2 for x in range(1,11)]
print("Cuadrados: ", squares)
#Cuadrados

#Grados celcius a fahrenheit

celsius=[0, 10, 20, 30, 40]
fahrenheit=[(temp * 9 / 5)+ 32 for temp in celsius]

print("Temperatura en fahrenheit: ", fahrenheit)


#Hallar numeros pares
evens=[x for x in range(1,21) if x%2 == 0 ]
evensImp=[y for y in range(1,21) if y%2 != 0 ]
print("Numeros pares: ",evens)
print("Numeros impares: ", evensImp)


#Matrices

matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

transposed=[[row[i] for row in matrix] for i in range(len(matrix[0]))]

#Los valores de i iran a cada fila y de esta manera se va iterando, 
# el nuevo valor es lo que se intercambia en la matriz

print(matrix)
print(transposed)


#Sin comprehesion lists hallar la transpuesta:

transposed=[]
for i in range(len(matrix[0])):
    transposed_row= []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)
