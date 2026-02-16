def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 18:
        return f'Com {idade} anos, o voto é NEGADO!'
    else:
        return f'Com {idade} anos, o voto é PERMITIDO!'
    
#Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
