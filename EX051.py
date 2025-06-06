PrimeiroTermo = int(input('Digite o primeiro termo da PA: '))
Razao = int(input('Digite a razão da PA: '))
decimo = PrimeiroTermo + 9 * Razao
for c in range (PrimeiroTermo,decimo,Razao):
    print(c)