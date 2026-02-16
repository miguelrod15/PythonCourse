equipas = list()
jogador = {}
jogos = list()

while True:                            #Começo apresentar jogadores
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    tot = int(input(f'Quantas jogos o {jogador["nome"]} disputou? '))
    jogos.clear()
    for c in range(0, tot):
        jogos.append(int(input(f'   Quantos golos no jogo {c+1}? ')))
    jogador['golos'] = jogos[:]
    jogador['total'] = sum(jogos)
    equipas.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    while True:
        if resp in 'SN':
            break
        print('ERRO! TENTE NOVAMENTE...')
    if resp == 'N':
        break                          #Final

print('-' * 40)
print('cod  ', end='')
for i in jogador.keys():               # trecho código para cabeçalho
    print(f'{i:<15}', end='')
print()
print('-' * 40)

for k, v in enumerate(equipas):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()
print('-' * 40)

while True:
    procura = int(input('Quer ver os dados de qual jogador? (999 para parar): '))
    if procura == 999:
        break
    if procura >= len(equipas):
        print(f'ERRO! Não existe nenhum jogador com código {procura}!')
    else:
        print(f' -- JOGADOR {equipas[procura]["nome"]}:')
        for i, g in enumerate(equipas[procura]['golos']):
            print(f'    No jogo {i+1} fez {g} golos')
    print('-' * 40)