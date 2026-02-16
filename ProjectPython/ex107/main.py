from ex107 import moeda

p = float(input('Escreva o preço: €'))
print(f'A metade de {p}€ é {moeda.metade(p)}€')
print(f'O dobro de {p}€ é igual a {moeda.dobro(p)}€')
print(f'Aumentado 20%, temos {moeda.aumentar(p, 20)}€')
print(f'Se diminuirmos 15%, temos {moeda.diminuir(p, 15)}€')