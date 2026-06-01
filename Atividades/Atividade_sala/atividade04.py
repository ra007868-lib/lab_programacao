notas = []
print("Digite suas 5 notas.")
for i in range(1, 6):
    notas_alunos = float(input(f"Digite sua {i}° nota: "))
    notas.append(notas_alunos)

menor_nota= min(notas)
notas.remove(menor_nota)

print(f"Menor nota: {menor_nota}")
print(f"Lista sem a menor nota: {notas}")
