Expressao = list(str(input("Digite a expressão: ")))
AbreParen = Expressao.count('(')
FechaParen = Expressao.count(')')
if AbreParen == FechaParen:
    print("Expressão válida!")
else:
    print("Expressão inválida!")