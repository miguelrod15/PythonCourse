from random import randint
computador = randint(0, 10)
print('Sou o seu computador, acabei de pensar em um número de 1 a 10?')
print('Será que voçê consegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite?:'))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente')
        elif jogador > computador:
            print('Menos... Tente novamente')
print('ACERTOU com {} tentativas. PARABÉNS!'.format(palpites))