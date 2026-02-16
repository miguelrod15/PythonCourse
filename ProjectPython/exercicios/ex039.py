from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento:'))
idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
elif idade > 18:
    saldo = idade - 18 
    print('Ja deveria ter feito o alistamento há {} anos'.format(saldo))
