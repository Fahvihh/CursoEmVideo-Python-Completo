def LeiaInt(msg):
    ok = False
    Valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            Valor = int(n)
            ok = True
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")
            LeiaInt(input("Digite um número inteiro: "))
        if ok:
            break
    return Valor


n = LeiaInt("Digite um número inteiro: ")
print(f"Você acabou de digitar o número {n}.")
