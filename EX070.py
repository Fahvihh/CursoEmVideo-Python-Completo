Tot = MaisMil = cont = Menor = 0
print("-_" *20)
print(" "*8, "LOJAO DAS PERIPÉCIAS")
print("-_" *20)
while True:
    Nome = str(input("Nome do produto: "))
    Preco = float(input("Preço: R$ "))
    Pergunta = str(input("Deseja continuar [S/N]: ")).upper()
    Tot += Preco
    cont += 1
    if cont == 1:
        Menor = Preco
    if Preco < Menor:
        Menor = Preco
    if Preco > 1000:
        MaisMil += 1
    if Pergunta == "N":
        break
print("-_" *20)
print(F"TOTAL GASTO: R${Tot:.2f}")
print(f"Havia {MaisMil} produtos acima de R$1000,00")
print(f"O menor preço foi de: R${Menor:.2f}")