Palavras = ('jujuba', 'picles', 'amendoim', 'sorvete', 'miojo', 'salmao', 'biscoito',
            'salada', 'mandioca', 'bacon', 'cheedar', 'calabresa', 'maionese', 'pamonha')
for p in Palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end ='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')