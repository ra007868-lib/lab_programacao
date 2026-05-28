lista = []
contador = 0
#coletando dados
for i in range(5):
    numero = int(input(f"Digite um {i + 1}°: "))
    lista.append(numero)
x = int(input("Digite o valor x: "))

posicao_encontrada = -1
i = 0

while i < 5:
    if lista[i] == x:
        posicao_encontrada = i
        break
    i += 1

print(posicao_encontrada)