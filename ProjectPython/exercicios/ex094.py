pessoal = list()                                                                
pessoa = dict()                                                                  
soma = média = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! TENTE NOVAMENTE...')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoal.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar?: [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO!! TENTE NOVAMENTE...')
    if resp == 'N':
        break
                                                                                                
print('-=' * 30)                                                                               #Parte 1 até aqui: Leitura dos dados

print(f'a) Ao todo foram cadastradas {len(pessoal)} pessoas')
média = soma / len(pessoal)
print(f'b) A média das idades é igual a {média:5.2f} anos.')
print(f'c) As mulheres cadastradas foram ', end='')
for p in pessoal:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print(f'd) Lista das pessoas acima da média: ')
for p in pessoal:
    if p['idade'] >= média:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<<<<<< ENCERRADO >>>>>>>>')                                                            #Parte 2: Analisando os dados - resultado