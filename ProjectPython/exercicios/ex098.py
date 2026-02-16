from time import sleep
def contador(i, f, p):
    if p == 0:   # Se o passo for 0, então vai de 1 em 1
        p = 1
    if p < 0:    # Se o passo for menor que 0 então o passo é igual a * -1
        p *= -1
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} -> ', end='', flush=True)    # Modo flush permite não haver bugs na mostragem do contador
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} -> ', end='',flush=True)
            sleep(0.5)
            cont -= p
        print('FIM')


#Programa principal
print('-=' * 20)
contador(1, 10, 1)
print('-=' * 20)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Inicio:  '))
fim = int(input('Fim:  '))
passo = int(input('Passo:  '))
contador(ini, fim, passo)
