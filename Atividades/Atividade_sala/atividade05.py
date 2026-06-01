lista = []
print("Digite 6 numeros inteiros abaixo...")
for i in range(6):
    numeros_digitados = int(input(f"Digite o {i+1}° numero inteiro: "))
    lista.append(numeros_digitados)

#numeros = [int(input(f"Digite o {i+1}. numero:)) for i in range(6)]

x = int(input(f"\Qual número deseja pasquisar? "))
ocorrencias = lista.count(x)
print("-"*30)
if ocorrencias >0:
    print(f"O número {x} aparece {ocorrencias} vez(es) na lista. ")
    print(f"Sua primeira aparição foi no índice: {lista.index(x)}")
else:
    print(f"O número {x} não foi encontrado na lista.")

    