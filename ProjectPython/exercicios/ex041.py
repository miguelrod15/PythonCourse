from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento:'))
idade = atual - nasc
print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classificação: Junior')
elif idade <= 25:
    print('Classificação: Senior')
else:
    print('Classificação: Master')