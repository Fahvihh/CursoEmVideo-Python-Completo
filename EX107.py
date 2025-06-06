from EX107Modulo import Moeda

N = float(input("Digite o preço: R$ "))
print(f"A metade de {N} é {Moeda.metade(N)}")
print(f"O dobro de {N} é {Moeda.dobro(N)}")
print(f"Aumento de 10% de {N} é {Moeda.aumentar(N)}")
print(f"Redução de 13% de {N} é {Moeda.reduzir(N)}")


