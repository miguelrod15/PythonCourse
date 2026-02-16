import moeda

p = float(input('Escreva o preço: €'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é igual a {moeda.dobro(p, True)}')
print(f'Aumentado 20%, temos {moeda.aumentar(p, 20, True)}')
print(f'Se diminuirmos 15%, temos {moeda.diminuir(p, 15, True)}')