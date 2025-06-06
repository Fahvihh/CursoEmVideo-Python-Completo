NomeCid = str(input('DIGITE O NOME DA SUA CIDADE: '))
if NomeCid.upper().find('SANTO') == 0:
    print(f'Sua cidade {NomeCid} começa com a palavra SANTO! Parabéns!')
else:
    print(f'Que pena, sua cidade {NomeCid} não começa com a palavra SANTO...')