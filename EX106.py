import time
def pyhelp(msg):
    while True:
        if msg == "FIM":
            break
        msg = str(input("\033[mDigite uma função: "))
        tam = len(f"ACESSANDO O MANUAL DO COMANDO '{msg}'...") + 4
        print(f"\033[1;32;43m{"-" * tam}")
        print(f"ACESSANDO O MANUAL DO COMANDO '{msg}'...")
        print(f"{"-" * tam}")
        print("\033[m")
        time.sleep(1)
        help(msg)
        print(f"\033[1;32;43m{"-" * tam}")


print("\033[1;30;45m=" *30)
print("   SITEMA DE AJUDA PYHELP")
print("=" *30)
resp = pyhelp("")