lista = []
pares = []
ímpares = []
while True:
    n = int(input('Escreve um valor: '))
    if n not in lista:
        lista.append(n)
    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta in 'Nn':
        print('=' * 40)
        print('A SUA LISTA ESTÁ TERMINADA')
        break

for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)

print('=' * 40)
print(f'A lista principal é a seguinte: {lista}')
print('=' * 40)
print(f'A lista pares é a seguinte: {pares}')
print('=' * 40)
print(f'A lista ímpares é a seguinte: {ímpares}')
print('=' * 40)
