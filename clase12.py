numbers=[1, 2, 3, 4, 5, 6]
for i in numbers:
    print('Aqui i es igual a : ',i+1)

for i in range(3,10):
    print(i)

fruits=["Manzana","Pera","Naranja","Mango","Banano"]
for fruit in fruits:
    print(fruit)
    if fruit=="Naranja":
        print("Naranja encontrada")

x=0
while x<5:
    if x==3:
        break
    print(x)
    x+=1


#continue para saltar iteraciones
numbers=[1, 2, 3, 4, 5, 6]
for i in numbers:
    if i==3:
        continue
    print('Aqui i es igual a : ',i)

# break para terminar iteraciones
    
numbers=[1, 2, 3, 4, 5, 6]
for i in numbers:
    if i==3:
        break
    print('Aqui i es igual a : ',i)