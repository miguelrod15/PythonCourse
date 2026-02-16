jogador = {}
jogos = list()
jogador['nome'] = str(input('Nome: '))
tot = int(input(f'Quantas jogos o {jogador["nome"]} disputou? '))
for c in range(0, tot):
    jogos.append(int(input(f'   Quantos golos no jogo {c}? ')))
jogador['golos'] = jogos[:]
jogador['total'] = sum(jogos)
print('-=' * 20)
print(jogador)
print('-=' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["golos"])} jogos.')
for i, v in enumerate(jogador['golos']):
    print(f'    => No jogo {i+1}, fez um total de {v} golos.')
print(f'Ao todo foram {jogador["total"]} golos.')
