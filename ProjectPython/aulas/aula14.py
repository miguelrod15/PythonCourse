n = 1
par = impar = 0
while n != 0:
    n = int(input('Escreva um valor: '))
    if n % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
print('Escreveu {} números par/es e {} números impar/es!'.format(par, impar))        