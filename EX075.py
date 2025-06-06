NumTupla = (int(input("Digite um valor: ")), int(input("Digite um outro valor: ")), int(input("Digite mais um valor: ")),
            int(input("Digite o último valor: ")))
print(NumTupla)
print(f"O valor 9 apareceu {NumTupla.count(9)} vezes")
if NumTupla.count(3) == 0:
    print("O valor 3 não foi digitado.")
else:
    print(f"O valor 3 foi digitado na posição: {NumTupla.index(3)+1}°")
pares = 0
for c in range(0,4):
    if NumTupla[c] % 2 == 0:
        pares += 1
print(f"Foram digitados {pares} valores pares")