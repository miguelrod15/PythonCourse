num = cont = soma = 0
while True:
    num = int(input('Escreva um número [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print('ACABOU!')
print(f'Foram apresentados {cont} números e a sua respetiva soma é igual a {soma}')
