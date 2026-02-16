maior = 0
menor = 0
for p in range (1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1: # Peso da 1ª pessoa
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('0 maior peso lido foi de {}Kg'.format(maior))
print('E o menor foi de {}Kg'.format(menor))