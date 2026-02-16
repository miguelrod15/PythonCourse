from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Miguel': randint(1, 6),
        'Mariana': randint(1, 6),
        'Martim': randint(1, 6),
        'Maria': randint(1, 6)}
ranking = list()
print('VALORES SORTEADOS')
for k, v in jogo.items():
    print(f'O/A {k} tirou {v}.')
    sleep(1)
print('-=' * 15)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)   # comando necessário para organizar por ordem do maior para o menor nos

print('=== RANKING DO JOGADORES ===')
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
print('-=' * 15)