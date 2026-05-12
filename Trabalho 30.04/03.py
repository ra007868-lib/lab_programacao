import random

lancamentos = []

contador = 0
while contador < 50:
    valor_dado = random.randint(1, 6)  # gera número entre 1 e 6
    lancamentos.append(valor_dado)
    contador += 1

ocorrencia_6 = []

posicao = 0
while posicao < 50:
    if lancamentos[posicao] == 6:
        ocorrencia_6.append(posicao)
    posicao += 1

print("Lançamentos do dado:")
print(lancamentos)

print("\nPosições onde apareceu a face 6:")
print(ocorrencia_6)