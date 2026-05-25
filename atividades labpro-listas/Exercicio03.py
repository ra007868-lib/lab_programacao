lista1 = [1, 2, 3, 4]
lista2 = [10, 20, 30, 40, 50, 60]
lista3 = []

for item1, item2 in zip(lista1, lista2):
    lista3.extend([item1, item2])
     
     
print(lista1)
print(lista2)
print(lista3)