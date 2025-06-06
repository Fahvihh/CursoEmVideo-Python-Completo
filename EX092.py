Pessoa = {}
Pessoa["Nome"] = str(input("DIGITE SEU NOME: "))
Pessoa["Idade"] = (2025 - int(input("DIGITE SEU ANO DE NASCIMENTO: ")))
Pessoa["CTPS"] = int(input("DIGITE O NÚMERO DA SUA CTPS [0 PARA NENHUMA]: "))
if Pessoa["CTPS"] != 0:
    Pessoa["Contratação"] = int(input("DIGITE O ANO DE CONTRATAÇÃO: "))
    Pessoa["Salário"] = float(input("DIGITE SEU SALÁRIO: "))
    Pessoa["Aposentadoria"] = Pessoa["Idade"] + ((Pessoa["Contratação"] + 35) - 2025)
for k, v in Pessoa.items():
    print(f"{k} tem o valor de: {v}")