def ficha(jog='<desconhecido>', golos=0):
    print(f'O jogador {jog} fez {golos} golo/os no campeonato')


#Programa principal
n = str(input("Nome do jogador: "))
g = str(input("Número de golos marcados: "))
if g.isnumeric():       # se o nº de golos puder ser um número inteiro vai receber um atributo do tipo int
    golos = int(g) 
else:                       # senão puder ser nº inteiro, tem de ser 0
    golos = 0
if n.strip() == '':      # se o nome for uma string vazia vai receber apenas o nº de golos 
    ficha(golos=g)
else:                       # senão recebe os 2 paramêtros opcionais
    ficha(n, g)