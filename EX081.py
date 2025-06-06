ListaNum = []
while True:
    ListaNum.append(int(input("Digite um valor: ")))
    Respota = str(input("Quer continuar? [S/N]: ")).upper()
    if Respota == "N":
        break
ListaNum.sort(reverse=True)
print("="*30)
print(f'Você digitou {len(ListaNum)} elementos')
print(f'A lista criada em ordem decrescente é: {ListaNum}')
if 5 in ListaNum:
    print(f'O valor 5 está contido na lista')
else:
    print(f'O valor 5 não está contido na lista')
