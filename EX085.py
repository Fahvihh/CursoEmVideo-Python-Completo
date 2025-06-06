ListaPares = list()
ListaImpares = list()
ListaGeral = [ListaPares, ListaImpares]
for c in range(1,8):
    Num = int(input("Digite um número inteiro: "))
    if Num % 2 == 0:
        ListaPares.append(Num)
    else:
        ListaImpares.append(Num)
print(f'Lista contendo a lista pares e a lista ímpares: {sorted(ListaGeral)}')
print(f'Lista Pares: {sorted(ListaGeral[0])}')
print(f'Lista Ímpares: {sorted(ListaGeral[1])}')