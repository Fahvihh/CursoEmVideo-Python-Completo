def validacao(N):
        while True:
            if N.isnumeric():
                N = float(N)
                break
            else:
                print("ERRO: Valor inválido")
                N = input("Digite um valor: ")
        return N



