from EX108Modulo import MoedaFormat
from EX107Modulo import Moeda

N = float(input("Digite o preço: R$ "))
print(f"A metade de {MoedaFormat.Moeda(N)} é {MoedaFormat.Moeda(Moeda.metade(N))}")
print(f"O dobro de {MoedaFormat.Moeda(N)} é {MoedaFormat.Moeda(Moeda.dobro(N))}")
print(f"Aumento de 10% de {MoedaFormat.Moeda(N)} é {MoedaFormat.Moeda(Moeda.aumentar(N))}")
print(f"Redução de 13% de {MoedaFormat.Moeda(N)} é {MoedaFormat.Moeda(Moeda.reduzir(N))}")
