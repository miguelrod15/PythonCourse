def área(larg, comp):
    a = larg * comp
    print(f'A área do terreno é {larg}x{comp} = {a:.2f}m²')


#Programa principal
print('-=' * 20)
print('            ÁREA DO TERRENO          ')
print('-=' * 20)
larg = float(input('LARGURA DO TERRENO (m): ' ))
comp = float(input('COMPRIMENTO DO TERRENO (m): ' ))
área(larg, comp)