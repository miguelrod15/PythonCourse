from random import randint
computador = randint(0,5) # A máquina sorteia um número

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? ')) # jogador tenta acertar o número
if jogador == computador:
    print('Parabéns! Acertou em cheio.')
else:
    print('PERDESTE! Pensei no número {} e não no número {}.'.format(computador, jogador))