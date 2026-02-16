cont = ( 'zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezasseis', 'dezassete', 'dezoito', 'dezanove', 'vinte')

while True:
    num = int(input('Escreva um valor entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Escreveste o número {cont[num]}')