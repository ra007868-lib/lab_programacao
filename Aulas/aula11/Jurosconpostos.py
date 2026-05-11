investimento_mensal=float(input("Quanto será investimento por mês: "))
taxa_juros_mensal=float(input("Qual a taxa de juros mesaç(1 para 1%)? "))/100

saldo = 0
ano_atual = 1
while True:
    # Processamento mês a mê (1ano = 12 interações)
    for mes in range(1, 13):
        # Adicione um aporte mensal ao saldo
        saldo +=investimento_mensal
        # Depois aplica os juros sobre saldo acumulado
        saldo +=saldo*taxa_juros_mensal


    # Saída do saldo após ciclo de 12 meses
    print(f"\nSaldo do investimeto após {ano_atual} ano(s): R${saldo: .2f}")

    # Verificar se continua no próximoano
    opcao=input("Deseja processar mais 1 ano:(S/N): ")

    if opcao == 'S':
        ano_atual+=1
    else:
        print("Simulação encerrada")
        break