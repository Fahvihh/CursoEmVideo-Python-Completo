Valor = input('Digite algo: ')
if Valor.isnumeric():
    print('O {} é numérico'.format(Valor))
else:
    print('O {} NÃO é numérico'.format(Valor))

if Valor.isalpha():
    print('O {} é alfabético'.format(Valor))
else :
    print('0 {} NÃO é alfabético'.format(Valor))
if Valor.isalnum():
    print('O {} é Alfanumérico'.format(Valor))
else:
    print('O {} NÃO é Alfanumérico'.format(Valor))
if Valor.islower():
    print('O {} tem apenas letras minúsculas'.format(Valor))
else:
    print('O {} NÃO tem letras minúsculas'.format(Valor))
if Valor.isupper():
    print('O {} tem apenas letras maiúsculas'.format(Valor))
else:
    print('O {} NÃO tem letras maiúsculas ou tem mistura'.format(Valor))
