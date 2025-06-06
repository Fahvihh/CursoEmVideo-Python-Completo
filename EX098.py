import time
def contador(a,b,c):
    for vezes in range(a,b,c):
        print(f"{vezes}", end=" ")
        time.sleep(0.5)

print("CONTAGEM [1,10,1]: ")
contador(1, 11, 1)
print("\n")
print("CONTAGEM [10,0,2]: ")
contador(10, -1, -2)
print('\n')
print("CONTAGEM [USUÁRIO]")
a = int(input("Digite o início: "))
b = int(input("Digite o fim: "))
c = int(input("Digite o passo: "))
if a > b:
    c = c * -1
contador(a, b+c, c)
print("FIM!!")
