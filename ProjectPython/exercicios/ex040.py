nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
media = (nota1 + nota2) / 2
print('Com as notas {:.1f} e {:.1f}, a média foi {:.1f}'.format(nota1, nota2, media))

if media < 5.0:
    print('A média é inferior a 5.0! REPROVADO')
elif 7.0 > media >= 5.0:
    print('A média permite RECUPERAÇÃO')
elif media >= 7.0:
    print('APROVADO')
