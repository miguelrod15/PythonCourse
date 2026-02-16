n = s = 0
while True:
    n = int(input('Escreva um valor: '))
    if n == 999:
        break   # comando break que acaba com a estrutura de loop
    s += n
print(f'A soma vale {s}') # f string - novo metódo atualizado