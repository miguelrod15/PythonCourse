print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos quer receber da sequência'))
print('~' * 30)
t1 = 0
t2 = 1
t3 = t2 + t1
print('~' * 30)
print('{} - {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t1 = t2
    t2 = t3
    cont = cont + 1
print(' - Fim')
