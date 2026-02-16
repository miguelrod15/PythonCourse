lista = ('Lápis', 1.75,
         'Borracha', 1.99,
         'Caderno', 10.90,
         'Estojo', 10,
         'Mochila', 20.99,
         'Canetas', 5.99,
         'Livro', 9.90)

print('-' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-' * 40)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'€{lista[pos]:>5.2f}')
print('-' * 40)
