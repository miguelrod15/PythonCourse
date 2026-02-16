preço = float(input('Preço das compras: €'))
print('''Formas de pagamento
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais''')

opção = int(input('Qual é a opção escolhida?'))
if opção == 1:
    total = preço - (preço * 0.10)
elif opção == 2:
    total = preço - (preço * 0.05)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra vai ser parcelada em 2x de €{:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 0.20)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de €{:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDA DE PAGAMENTO. Tente novamente')

print('Sua compra de €{:.2f} vai custar €{:.2f} no final '.format(preço,total))