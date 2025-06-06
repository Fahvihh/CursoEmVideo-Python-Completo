from EX109Modulo.moeda import aumentar, dobro, reduzir
from EX109Modulo.moeda import metade, Moeda

N = float(input("Digite o preço: R$ "))
print(f"A metade de {Moeda(N)} é {metade(N, True)}")
print(f"O dobro de {Moeda(N)} é {dobro(N, True)}")
print(f"Aumento de 10% de {Moeda(N)} é {aumentar(N, True)}")
print(f"Redução de 13% de {Moeda(N)} é {reduzir(N, True)}")