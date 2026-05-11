n1 = input("Digite seu nome: ")
n2 = input("Digite seu nome: ")
n3 = input("Digite seu nome: ")
nt1 = float(input(f"Nota de {n1}: "))
nt2 = float(input(f"Nota de {n2}: "))
nt3 = float(input(f"Nota de {n3}: "))
media = (nt1 + nt2 + nt3)/3
print(f"A média da turma é {media:.2f}")
if nt1 > media:
    print(f"Parabéns {n1}, sua nota {nt1}")
if nt2 > media:
    print(f"Parabéns {n2}, sua nota {nt2}")
if nt3 > media:
    print(f"Parabéns {n3}, sua nota {nt3}")