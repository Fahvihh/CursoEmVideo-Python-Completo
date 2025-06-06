def voto(DataNasc):
    from datetime import date
    idade = date.today().year - DataNasc
    if idade < 16:
        return f"VOCÊ TEM: {idade} ANOS. VOTO NEGADO."
    elif 18 <= idade <= 65 :
        return f"VOCÊ TEM: {idade} ANOS. VOTO OBRIGATÓRI0."
    else:
        return f"VOCÊ TEM: {idade} ANOS. VOTO OPCIONAL."


voto(int(input("Digite seu ano de nascimento: ")))