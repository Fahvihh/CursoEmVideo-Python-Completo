def notas(*n,sit=False):
    '''
    Função criada para cálculo de notas - Criado por Fatima Vitória.
    :param n: notas do estudante.
    :param sit: situação do aluno, True = Aparece aprovado ou reprovado dependendo da nota, False = Não aparece.
    :return: retorna r que é um dicionário contendo o total de notas, a maior nota, a menor nota, a média e se desejado, a situação.
    '''
    r = dict()
    r["Total"] = len(n)
    r["Maior Nota"] = max(n)
    r["Menor Nota"] = min(n)
    r["Média"] = sum(n) / len(n)
    if sit:
        if r["Média"] >= 6:
            r["Situação"] = "APROVADO"
        else:
            r["Situação"] = "REPROVADO"

    return r


Resp = notas(8.9, 9.5, 6.5, 9, 7.9, 10, sit = True )
print(Resp)
help(notas)