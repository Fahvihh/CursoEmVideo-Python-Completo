def maior(*num):
    tam = len(num) + 50
    print(f"{"*"*tam}")
    print("Analisando os valores passados...")
    print(f'{num}', end=" ")
    print(f"Foram informados {len(num)} valores ao todo.")
    print(f"O maior valor informado foi: {max(num)}")
    print(f"{"*" * tam}")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)