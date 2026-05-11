qtda_alunos = 10
nomes = []
notas = []
media = 0
for i in range(qtda_alunos):
    nomes.append(input(f"Nome do aluno {i+1}°:"))
    notas.append(float(input(f"Nota de {nomes[i]}: ")))
    media = media + notas[i]

media = media / qtda_alunos
print(f"\n a media da turma é {media:.2f}.\n")
print("alunos com notas acima da media:")
for i in range(qtda_alunos):
    if notas[i] > media:
        print(f"Parabens {nomes[i]}! Suanota foi {notas[i]:.1f}")

print(nomes,notas)