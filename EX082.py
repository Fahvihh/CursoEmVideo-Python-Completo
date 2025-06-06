ListaCompleta = []
ListaPares = []
ListaImpares = []
while True:
    Valor = int(input("Digite um valor inteiro: "))
    Resposta = str(input("Quer continuar? [S/N]: ")).upper()
    ListaCompleta.append(Valor)
    if Valor % 2 == 0:
        ListaPares.append(Valor)
    else:
        ListaImpares.append(Valor)
    if Resposta == "N":
        break
print(f'A lista completa é: {ListaCompleta}')
print(f'Os valores pares são: {ListaPares}')
print(f'Os valores ímpares são: {ListaImpares}')