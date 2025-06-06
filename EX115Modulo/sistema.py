from EX115Modulo.Lib.Arquivo import ArquivoExiste
from EX115Modulo.Lib.interface import *
from EX115Modulo.Lib.Arquivo import *
from time import sleep


arq = "CursoemVideo.txt"
if not ArquivoExiste(arq):
    CriarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoa', 'Sair do sistema'])
    if resposta == 1:
        LerArquivo(arq)
    elif resposta == 2:
        cabecalho("CADASTRO DE PESSOAS")
        nome = str(input("Nome: "))
        idade = int(input("Idade: "))
        Cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho("Saindo do sistema...")
        break
    else:
        print("\033[0;31mERRO: Digite um valor entre 1 e 3!\033[m")
    sleep(2)