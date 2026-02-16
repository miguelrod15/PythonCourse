salário = float(input('Qual é o salário do funcionário?: EUR$'))
if salário <= 1250:
    novo = salário + (salário * 0.15)
else:
    novo = salário + (salário * 0.10)

print('Quem ganhava EUR${:.2f} passa a ganhar EUR${:.2f} agora'.format(salário, novo))