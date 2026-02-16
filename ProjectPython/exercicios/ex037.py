num = int(input('Escreva um número inteiro:'))
print('''Escolha uma das bases para conversão:
[1] Converter para Binário
[2} Converter para Octal
[3] Converter para Hexadecimal ''')

opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Essa opção não existe')
