num = (int(input('Escreva um número: ')),
       int(input('Escreva outro número: ')),
       int(input('Escreva mais um número: ')),
       int(input('Escreva o último número: ')))
print('=' * 30)
print(f'Escreveste os valores {num}')
print('=' * 30)
print(f'O número 9 apareceu {num.count(9)} vezes')
print('=' * 30)
if 3 in num:
    print(f'o primeiro valor 3 foi escrito na posição {num.index(3)+1}')
else:
    print('O valor 3 não foi escrito em nenhuma posição')
print('=' * 30)
print(f'Os números pares escritos foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
