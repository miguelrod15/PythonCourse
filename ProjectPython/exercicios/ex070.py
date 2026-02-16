totgasto = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Escreva um produto: '))
    preço = float(input('Qual é o preço do produto?: € '))
    cont += 1
    totgasto += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi {totgasto}')
print(f'O total de produtos acima de 1000€ foram {totmil}')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}€')
    