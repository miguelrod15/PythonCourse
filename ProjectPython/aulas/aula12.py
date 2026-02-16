nome = str(input('Qual é o nome?:'))
if nome == 'Miguel':
    print('Que belo nome!')
elif nome == 'Pedro' or nome == 'Mou' or nome == 'Deus':
    print('O seu nome é bem popular')
elif nome in 'Poao Vicente':
    print('Belo nome')
else:
    print('Nome bem normal')
print('Tenha um bom dia, {}!'.format(nome))
