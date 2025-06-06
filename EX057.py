sexo = str(input('Digite o sexo [M/F]: ')).upper()
while sexo != "M" and sexo != 'F':
    print('Valor incorreto. Por favor digite novamente')
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
if sexo == 'M':
    print('Sexo digitado é Masculino.')
elif sexo == 'F':
    print('Sexo digitado é Feminino')