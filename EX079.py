ListaValor = []
cont = 0
Resposta = ''
while True:
    Valor = int(input("Digite um valor: "))
    if cont == 0:
        ListaValor.append(Valor)
        print("Valor Adicionado!")
    else:
        if Valor in ListaValor:
            print("Valor duplicado! Não irei adicionar")
        else:
            ListaValor.append(Valor)
            print("Valor Adicionado!")
    Resposta = str(input("Quer continuar? [S/N]: ")).upper()
    cont +=1
    if Resposta == "N":
        break
print(sorted(ListaValor))
