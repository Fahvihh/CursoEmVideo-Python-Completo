dados1 = list()
dados2 = list()
dados3 = list()
Linha1 = list()
Linha2 = list()
Linha3 = list()
Pares = list()
Impares = list()
MaiorL2 = 0
for c in range(0,3):
    dados1.append(int(input(f"Digite um valor para [0, {c}]: ")))
    Linha1.append(dados1[:])
    if dados1[0] % 2 == 0:
        Pares.append(dados1[0])
    else:
        Impares.append(dados1[0])
    dados1.clear()
for c in range(0,3):
    dados2.append(int(input(f"Digite um valor para [1, {c}]: ")))
    Linha2.append(dados2[:])
    if dados2[0] % 2 == 0:
        Pares.append(dados2[0])
    else:
        Impares.append(dados2[0])
    dados2.clear()
for c in range(0,3):
    dados3.append(int(input(f"Digite um valor para [2, {c}]: ")))
    Linha3.append(dados3[:])
    if dados3[0] % 2 == 0:
        Pares.append(dados3[0])
    else:
        Impares.append(dados3[0])
    dados3.clear()
print(" "*5 ,"MATRIZ GERADA")
print("=*"*20)
print(f'  {Linha1[0]}     {Linha1[1]}     {Linha1[2]}  ')
print(f'  {Linha2[0]}     {Linha2[1]}     {Linha2[2]}  ')
print(f'  {Linha3[0]}     {Linha3[1]}     {Linha3[2]}  ')
print("=*"*20)
print(f'ÍMPARES: {Impares}')
print(f'PARES: {Pares}')
print(f'SOMA DOS PARES: {sum(Pares)}')
print(f'A SOMA DOS VALORES DA 3° COLUNA: {sum(Linha1[2] + Linha2[2] + Linha3[2])}')
if Linha2[0] > Linha2[1] and Linha2[0] > Linha2[2]:
    MaiorL2 = Linha2[0]
elif Linha1[1] > Linha1[0] and Linha1[1] > Linha2[2]:
    MaiorL2 = Linha2[1]
else:
    MaiorL2 = Linha2[2]
print(f'O MAIOR VALOR DA LINHA 2: {MaiorL2}')
print("=*"*20)