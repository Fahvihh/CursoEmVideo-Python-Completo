def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")
            continue
        else:
            return n

def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print("\033[0;31mERRO! Digite um número real válido.\033[m")
            continue
        except KeyboardInterrupt:
            print("\033[0;31mERRO! Sem valores digitados.\033[m")
            return 0
        else:
            return n


i = LeiaInt("Digite um número inteiro: ")
r = LeiaFloat("Digite um valor real: ")
print(f"Você acabou de digitar o número {i}")
print(f"Você acabou de digitar o número {r}")

