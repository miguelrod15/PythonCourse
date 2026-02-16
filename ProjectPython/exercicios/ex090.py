aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

if aluno['Média'] >= 9.5:
    aluno['Nota'] = 'Aprovado'
elif 7<= aluno['Média'] < 9.5:
    aluno['Nota'] = 'Recuperação'
else:
    aluno['Nota'] = 'Reprovado'
print('-=' * 30 )
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')