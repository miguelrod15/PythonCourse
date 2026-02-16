#======================= TUPLAS ===============================
lanche = 'Hambúrger', 'Sumo', 'Pizza', 'Pudim', 'Gelado'
for comida in lanche:     # Forma 1 de verificar uma tupla com estrutura de repetição for
    print(f'EU vou comer {comida}')

for pos, comida in enumerate(lanche):   # Forma 2 de verificar uma tupla com estrutura de repetição for, precisando da posição
    print(f'Eu vou comer {comida} na posição {pos}')

for cont in range (0, len(lanche)): #Forma 3 de verificar uma tupla com estrutura de repetição for, precisando da posição
    print(f'EU vou comer {cont}')

print(sorted(lanche))   # comando sorted que organiza a tupla