cont = 0
while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    cont += 1
    print(20*"*","TABUADA",20*"*")
    for cont in range(1,11):
        print(f"{num} x {cont} = {num*cont}")
print("FIM DO PROGRAMA!!")