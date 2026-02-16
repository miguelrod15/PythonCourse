from random import randint
from time import sleep

def sorteia(list):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        list.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('READY!')
        

def somaPar(list):
    soma = 0
    for valor in list:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando todos os valores pares de {list}, temos {soma}')

números = list()
sorteia(números)
somaPar(números)