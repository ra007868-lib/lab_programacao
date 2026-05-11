# 1. Faça um programa que leia dos vetores de tres posiçoes, que representam forças sobre um ponto no espaço 3D, e escreva
print("informe as cordenadas da primeira força (F1)")
f1 = []
f1.append(float(input("F1 - x: ")))
f1.append(float(input("F1 - y: ")))
f1.append(float(input("F1 - z: ")))

print("informe as cordenadas da segunda força (F2)")
f2 = []
f2.append(float(input("F2 - x: ")))
f2.append(float(input("F2 - y: ")))
f2.append(float(input("F2 - z: ")))

rx = f1[0] + f2[0]
ry = f1[1] + f2[1]
rz = f1[2] + f2[2]

forca_resultante = [rx,ry,rz]

print("-" * 60)
print(f'A força resultante no espaço 3D é: {forca_resultante}')
print(f'Componentes individuasis -> X:{rx}, Y:{ry}, Z:{rz}')