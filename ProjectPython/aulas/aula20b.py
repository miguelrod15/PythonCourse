def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Escreva um número: '))
if par(num):
    print('É par')
else:
    print('É ímpar')