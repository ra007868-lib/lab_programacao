import random

lista1 = []
for i in range(100):
    numeros = random.randint(1, 6)
    lista1.append(numeros)

lista2 = []
for face in range(1,7):
    quantidade = lista1.count(face)
    lista2.append(quantidade)
print("Vetor de lançamento (100 vezes)")
print(lista1)
print("\nVetor de frequências (Quantidade de vezes dss faces: 1, 2, 3, 4, 5, 6)")
print(lista2)

