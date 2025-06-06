ListaNum = []
Maior = Menor = 0
for c in range(0,5):
    num = int(input(f"Digite o valor da posição {c}: "))
    ListaNum.append(num)
    if c == 1:
        Maior = num
        Menor = num
    else:
        if num > Maior:
            Maior = num
        elif num < Menor:
            Menor = num
print(f'A lista digitada foi: {ListaNum}')
print(f'O maior valor foi {Maior} encontrado na posição: ', end='')
for p, d ,in enumerate(ListaNum):
    if d == Maior:
        print(f"{p}...", end='')
print(f'\nO menor valor foi {Menor} encontrado na posição: ', end='')
for p, d ,in enumerate(ListaNum):
    if d == Menor:
        print(f"{p}...", end='')