#-----------------------------DICTIONARIES------------------------------

#pessoas = {'nome': 'Gustavo', 'sexo':'M', 'idade': 22}
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos e pertence ao sexo {pessoas["sexo"]}')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
# pessoas['peso'] = 75.5
#for k, v in pessoas.items():
    #print(f'{k} : {v}')

#brasil = []
#estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
#brasil.append(estado1)
#brasil.append(estado2)
#print(brasil[0])

estado = dict()
brasil = list()
for c in range (0, 3):        # for para alimentar a lista
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
print(brasil)
print('=' * 30)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
