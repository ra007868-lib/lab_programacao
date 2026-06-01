while True:
    num = int(input("Digite um numero (ou 0 para sair)"))
    if num == 0:
        print("Encerrado...")
        break
    if num >=10 and num <=50:
        print("Dado válido!")
    else:
        print("Dado inválido!")
