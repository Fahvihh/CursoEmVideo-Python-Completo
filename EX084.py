ListaPessoas = list()
ListaGeral = list()
MaiorPeso = MenorPeso = 0
while True:
    ListaPessoas.append(str(input("Digite o nome: ")))
    ListaPessoas.append(float(input("Digite o peso: ")))
    if len(ListaGeral) == 0:
        MaiorPeso = MenorPeso = ListaPessoas[1]
    else:
        if ListaPessoas[1] > MaiorPeso:
            MaiorPeso = ListaPessoas[1]
        if ListaPessoas[1] < MenorPeso:
            MenorPeso = ListaPessoas[1]
    ListaGeral.append(ListaPessoas[:])
    ListaPessoas.clear()
    Resposta = str(input("Quer continuar? [S/N]: ")).upper()
    if Resposta == "N":
        break
print("=="*20)
print(f'Os dados foram: {ListaGeral}')
print(f'Ao todo foram cadastradas {len(ListaGeral)} pessoas')
print(f'O maior peso foi {MaiorPeso}KG.Sendo a ou as pessoas: ', end='')
for p in ListaGeral:
    if p[1] == MaiorPeso:
        print(f'{p[0]}', end='')
print(f'O menor peso foi {MenorPeso}KG.Sendo a ou as pessoas: ',end='')
for p in ListaGeral:
    if p[1] == MenorPeso:
        print(f'{p[0]}', end='')