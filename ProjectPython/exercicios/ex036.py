casa = float(input('Qual é o valor da casa?: €$'))
salario = float(input('Salário do comprador?: €$'))
anos = int(input('Anos de financiamento?:'))
prestação = casa / (anos * 12)
minimo = salario * 0.30
 
print('Para pagar uma casa de €${:.2f} em {} anos'.format(casa, anos))
print('A prestação será de €${:.2f}'.format(prestação))

if prestação <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
 