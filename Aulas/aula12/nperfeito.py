n_desejado = int(input("Quantos números perfeitos você quer encontrar?"))
encontrados = 0
numero_testado = 2 # começamos do 2 (1 não é perfeito)
print(f"Buscando os {n_desejado} primeiro número perfeito")
while encontrados < n_desejado:
    soma_divisores = 0
    # Encontra os dovisores do "numero_testado"
    for i in range (1, numero_testado):
        if numero_testado % i == 0:
            soma_divisores += i
    #verificar se a soma é igual ao número
    if soma_divisores == numero_testado:
        encontrados += 1
        print(f"{encontrados}. número perfeiro encontrado: {numero_testado}")
    numero_testado += 1
