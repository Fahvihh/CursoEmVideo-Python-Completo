Nome = str(input("Digite o nome do aluno: "))
media = float(input("Digite a média do aluno: "))
pessoa = {"nome": Nome, "média": media}
if media >= 6.0:
    pessoa["Situação"] = 'Aprovado'
else:
    pessoa["Situação"] = 'Reprovado'
for k, v in pessoa.items():
    print(f"{k} é igual a: {v}")