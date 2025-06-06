import urllib
import urllib.request

def VerificaSite(link):
    try:
        if urllib.request.urlopen(link):
            print("Site Verificado com sucesso!")
    except:
        print(f'Sem acesso ao site {link}')

VerificaSite('https://www.pudim.com.br')