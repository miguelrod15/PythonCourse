numeros = list()

while True:
    n = int(input('Escreva um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado, não consigo adicionar...')
    r = str(input('Quer continuar?: [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        print('Lista completa!')
        break
print('=' * 40)
numeros.sort()
print(f'Os valores presentes na lista são {numeros}')