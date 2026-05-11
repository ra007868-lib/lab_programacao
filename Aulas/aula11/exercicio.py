while True:
    num=int(input("\nDigite um numero inteiro positivo: "))
    # conta divisores
    qtde_divisores= 0
    print(f"Divisores de {num}: ",end="")
    # loop para encontrar e exibir os divisores
    for i in range(1, num+1):
        if num%i==0:
            print(i, end=" ") #exibe os divisores
            qtde_divisores +=1

    #Verificar se o número é primo baseado na quantidade
    print()
    if qtde_divisores == 2:
        print(f"Conclusão: O número é PRIMO")
    else:
        print:(f"Conclusão: o número {num} NÂO é primo (possui {qtde_divisores} divisores)")


    # opção para inserir novo número
    continuar=input("\nDeseja analisar outro número?(S/N): ").upper()
    if continuar != 'S':
        break


