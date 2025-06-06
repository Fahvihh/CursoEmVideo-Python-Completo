from EX110Modulo import dobro, Moeda, metade, reduzir, aumentar


def Resumo(N, Reducao, aumento):
    print("=" * 40)
    print("   -------- RESUMO DO VALOR --------")
    print("="*40)
    print(f"Preço analisado: {Moeda(N)}")
    print(f"Dobro do preço: {dobro(N, True)}")
    print(f"Metade do preço: {metade(N, True)}")
    print(f"{aumento}% de aumento: {aumentar(N, aumento, True)}")
    print(f"{Reducao}% de redução: {reduzir(N, Reducao, True)}")
    print("="*40)
