valores = []
contador_vezes = 0
contador_diferentes = 0

#coletando dados
for i in range(10):
    numero = int(input(f"Digite um {i + 1}°: "))

    encontrado = False
    posicao = 0

    while posicao < contador_vezes:
        if valores[posicao] == numero:
            encontrado = True
        posicao += 1
    
    if not encontrado:
        contador_diferentes += 1

    valores.append(numero)
    contador_vezes += 1
#Resultado
print("Quantidade de valores diferentes:", contador_diferentes)