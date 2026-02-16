temp = []
princ = []
totmaior = totmenor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: Kg')))
    if len(princ) == 0:
        totmaior = totmenor = temp[1]
    else:
        if temp[1] > totmaior:
            totmaior = temp[1]
        if temp[1] < totmenor:
            totmenor = temp[1]
    princ.append(temp[:])
    temp.clear()

    
    resp = str(input('Deseja continuar?: [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('=' * 40)
print(f'Ao todo a lista tem {len(princ)} registos.')
print('=' * 40)
print(f'O maior peso foi de {totmaior}Kg. Peso de ', end='')
for p in princ:
    if p[1] == totmaior:
        print(f'{p[0]} ', end='')
print()
print(f'O menor peso foi de {totmenor}Kg. Peso de ', end='')
for p in princ:
    if p[1] == totmenor:
        print(f'{p[0]} ', end='')
print()