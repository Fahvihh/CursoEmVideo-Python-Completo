Nome = str(input('DIGITE SEU NOME COMPLETO: ')).split()
print(f'Seu primeiro nome é: {Nome[0].title()}')
print(f'Seu último nome é: {Nome[len(Nome)-1].title()}')
