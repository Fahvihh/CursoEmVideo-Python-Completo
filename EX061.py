PrimeiroTermo = int(input('Digite o primeiro termo da PA: '))
Razao = int(input('Digite a razão da PA: '))
cont = 0
print(PrimeiroTermo)
while cont <= 8:
    cont += 1
    termos = PrimeiroTermo + cont * Razao
    print(termos)