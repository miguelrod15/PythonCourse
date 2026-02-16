numeros = []
while True:
    n = int(input('Escreva um valor: '))
    if n not in numeros:
        numeros.append(n)
    resposta = str(input('Quer continuar?: [S/N] ')).strip().upper()[0]
    
    if resposta in 'Nn':
        print('=' * 35)
        print('LISTA TERMINADA COM SUCESSO')
        break
    
print('=' * 35)
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
print(f'A lista contém {len(numeros)} elementos')

if 5 in numeros:
    print('SIM, o 5 faz parte da lista')
else:
    print('NÃO, o 5 não faz parte da lista')
