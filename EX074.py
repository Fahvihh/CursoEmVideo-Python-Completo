import random
NumTupla = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10),
       random.randint(1,10))
print(NumTupla)
print(f'O maior valor sorteado foi: {sorted(NumTupla)[-1]}')
print(f'O menor valor sorteado foi: {sorted(NumTupla)[0]}')