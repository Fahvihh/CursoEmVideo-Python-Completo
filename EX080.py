ListaNum = []
for c in range(0,5):
    Num = int(input("Digite um número: "))
    if c == 0 or Num > ListaNum[-1]:
        print("Adicionado ao final da lista...")
        ListaNum.append(Num)
    else:
        pos = 0
        while pos < len(ListaNum):
            if Num <= ListaNum[pos]:
                ListaNum.insert(pos, Num)
                print(f"Adicionado na posição {pos}° da lista...")
                break
            pos += 1
print(ListaNum)