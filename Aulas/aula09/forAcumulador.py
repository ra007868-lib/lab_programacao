num = int(input("Digite um numero:"))
num_1 = int(input("Digite o segundo numero maior que o primeiro: "))
soma = 0
for i in range (num, num_1 + 1):
        if(i%2 == 0):
            soma = soma + i       
print("A soma é", soma)
