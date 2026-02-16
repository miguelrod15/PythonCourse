from time import sleep
def maior(* num):
    cont = maior = 0
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados ao todo {cont} valores.')
    print(f'O maior valor informado foi {maior}.')

# Programa principal
maior(2, 7, 2, 1, 9, 0, 4)
maior(5, 7, 2, 0)
maior(0, 6, 6)
maior(0)
maior()