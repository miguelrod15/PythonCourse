###===========================Listas========================##
# num = [2, 5, 9, 6, 8, 3, 0]
# num [2] = 7  # Troca o número na posição definida
# num.append(1)  # comando append adiciona à lista
# num.sort(reverse=True) ## Comando sort organiza por ordem decrescente
# num.insert(2, 0)
# num.pop(2)

#valores = []
#valores.append(5)
#valores.append(7)
#valores.append(9)

#valores = list()
#for cont in range (0, 5):
    #valores.append(int(input('Escreva um valor: ')))

#for c, v in enumerate(valores):
    #print(f'Na posição {c} encontrei o valor {v}!')
#print('Cheguei ao final da lista...')


a = [2, 3, 5, 7, 8]
b = a[:]
b[2] = 2
print(f'Lista A: {a}')
print(f'Lista B: {b}')