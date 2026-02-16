equipas = ('Benfica', 'Porto', 'Sporting', 'Braga',
           'Vitória SC', 'Moreirense', 'Arouca', 'Estoril',
           'Alverca', 'Rio Ave', 'AFS', 'Famalicão',
           'Tondela', 'Casa Pia', 'Estrela', 'Santa Clara',  
           'Nacional')
print('=' * 30)
for t in equipas:
    print(t)
print('-=' * 30)
print(f'As 5 primeiras equipas são {equipas[0:5]}')     #Quero ver quem são as 5 primeiras equipas 
print('-=' * 30)
print(f'Os 4 últimos classificados são {equipas[-4:]}')
print('-=' * 30)
print(f'Tudo organizado de forma alfabética fica {sorted(equipas)}')
print('-=' * 30)
print(f'O Famalicão está na posição {equipas.index('Famalicão')+1}')
print('-=' * 30)
