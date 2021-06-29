from random import randint
from time import sleep
from operator import itemgetter

dados = dict()

for i in range(1,5):
    dados[i] = randint(1,6)
    print(f'O jogador{i} tirou {dados[i]} no dado.')
    sleep(1)

print("-=" * 20)
print("==RANKING DOS JOGADORES==")

lista = list()
lista = sorted(dados.items(), key = itemgetter(1), reverse = True) # ordena chave e valor do dicionario em ordem decrescente (reverse=True) de VALOR --> itemgetter(1)
print(lista)

for i,v in enumerate(lista):
    print(f'{i+1}° lugar: jogador{v[0]} com {v[1]}', end = ' ') 
    print()
    sleep(1)
        