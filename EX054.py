maiores = 0
menores = 0
for c in range(1,8):
    AnoNasc = int(input('Digite seu ano de nascimento: '))
    if (2025 - AnoNasc) >= 18:
        maiores += 1
    else:
        menores += 1
print(f'Ao todo {maiores} atingiram a maioridade e {menores} NÃO atingiram ainda.')