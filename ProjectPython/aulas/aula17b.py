pessoas = list()
dados = list()
totmaior = 0
totmenor = 0
for c in range (0, 3): 
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:])
    dados.clear()
print(pessoas)

for p in pessoas:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade')