import time
from datetime import datetime
print('Olá Querido! Vamos calcular se você já deve se alistar no exército ou não!')
DataNasci = int(input('DIGITE SEU ANO DE NASCIMENTO: '))
print('CALCULANDO...')
time.sleep(2.0)
Datahoje= datetime.now().year
if Datahoje - DataNasci == 18:
    print('Você tem exatos 18 anos! Está na hora de se alistar!')
elif Datahoje - DataNasci < 18:
    print(f'Ufa! Ainda não precisa, apenas daqui há {18-(Datahoje-DataNasci)} anos')
else:
    print(f'Vixe! Já passou da hora de você se alistar! Você está há {(Datahoje-DataNasci)-18} anos atrasado!')