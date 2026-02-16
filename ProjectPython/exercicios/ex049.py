num = int(input('Escreva um número para ver a sua tabuada: '))
for c in range(1, 11):
    print('{} x {:1} = {}'.format(num, c, num*c))