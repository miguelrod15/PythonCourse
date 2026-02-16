from random import randint
total = 0
wins = 0
while True:    # Aqui criou-se o primeiro true para escolher o número do jogador e o computador escolher o seu, juntando os 2
    jogador = int(input('Escolhe um valor: '))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':   # Criou-se outro while para definir se a string é a certa, ou seja o Par ou ímpar
        tipo = str(input('Par ou ímpar? [P/I]: ')).strip().upper()[0]
        print(f'Escolheste o número {jogador} e o computador {computador}. O total originou {total}. ', end='')
        print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('GANHASTE')
            wins += 1
        else:
            print('PERDESTE')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('GANHASTE!')
            wins += 1
        else: 
            print('PERDESTE!')
            break
    print('Vamos jogar novamente')
print(f'GAME OVER! Ganhaste {wins} vezes.')
    





        

    


