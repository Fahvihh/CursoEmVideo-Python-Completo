def escreva(msg):
    tam = len(msg) + 4
    print(f"{"-"*tam}")
    print(f'  {msg}')
    print(f"{"-"*tam}")


escreva(str(input("Digite uma mensagem: ")))