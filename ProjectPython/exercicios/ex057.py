sexo = str(input('Informa o seu sexo: [M/F]: ')).strip().upper()[0]  # Strip(Sem espaços), Upper(Letra grande) e [0} - ver a 1ª letra apenas
while sexo not in 'MF':
    sexo = str(input('Dados inválidos, informe seu sexo:')).strip().upper()[0]
print('O sexo {} foi registrado com sucesso'.format(sexo))