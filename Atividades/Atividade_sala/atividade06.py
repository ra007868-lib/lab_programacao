nome_originais = []
for i in range(5):
    nome = input(f"Digite o {i+1}° nome: ")
    nome_originais.append(nome)
nomes_invertidos =[]
for i in range(1,6):
    nomes_invertidos.append(nome_originais[-i])

print(nome_originais)
print(nomes_invertidos)