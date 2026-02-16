print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA:'))
termo = primeiro 
cont = 1
total = 0    # Variável total de termos começa em 0
mais = 10    # Variável mais começando nos 10 primeiros termos
while mais != 0:    # Estrutura while enquanto for diferente de 0
    total = total + mais
    while cont <= total:    # Estrutura while enquanto o contador é menor ou igual que o total
        print('{} - '.format(termo), end='')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos quer acrescentar a mais?'))
print('Progressão acabada com {} termos mostrados'.format(total))
