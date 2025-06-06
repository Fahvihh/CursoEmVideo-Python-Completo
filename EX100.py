import random
listnums = list()
par = list()
def sorteia():
    for c in range(1,6):
        nums = random.randint(1,10)
        listnums.append(nums)
    print(f"Valores sorteados: {listnums}")
def somapar():
    for x in range(0, 5):
        if listnums[x] % 2 == 0:
            par.append(listnums[x])
    print(f"SOMA dos pares: {sum(par)}")


sorteia()
somapar()