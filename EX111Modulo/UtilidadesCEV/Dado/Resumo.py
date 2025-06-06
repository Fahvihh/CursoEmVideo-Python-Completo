from EX111Modulo.UtilidadesCEV import Moeda


def resumo(N, Reducao, aumento):
    print("=" * 40)
    print("   -------- RESUMO DO VALOR --------")
    print("="*40)
    print(f"Preço analisado: {Moeda.Moeda(N)}")
    print(f"Dobro do preço: {Moeda.dobro(N, True)}")
    print(f"Metade do preço: {Moeda.metade(N, True)}")
    print(f"{aumento}% de aumento: {Moeda.aumentar(N, aumento, True)}")
    print(f"{Reducao}% de redução: {Moeda.reduzir(N, Reducao, True)}")
    print("="*40)