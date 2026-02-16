import moeda

p = float(input('Escreva o preço: €'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é igual a {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentado 20%, temos {moeda.moeda(moeda.aumentar(p, 20))}')
print(f'Se diminuirmos 15%, temos {moeda.moeda(moeda.diminuir(p, 15))}')