somaidade = 0
mediaidade = 0
idadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range (1, 5):
    print('------------ {}ª PESSOA ------------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    
    if p == 1 and sexo in 'Mm': # Sobre a 1ª pessoa e se é Masculina
        idadehomem = idade 
        nomevelho = nome 
    
    if sexo in 'Mm' and idade > idadehomem: # Se a 2ªa pessoa ainda for homem
        idadehomem = idade
        nomevelho = nome
    
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print('A média do grupo é {}'.format(mediaidade))
print('O homem mais velho tem {} anos e chama-se {}'.format(idadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))