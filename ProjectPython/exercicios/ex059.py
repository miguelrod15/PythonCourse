n1 = int(input('Escreva um número: '))
n2 = int(input('Escreva outro número: '))
opção = 0
soma = 0
while opção != 5:    # enquanto a opção for difente de 5 quero que faça as seguintes funcionalidades...
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opção = int(input('>>>>>>>> Que opção deseja escolher?:'))
    if opção == 1:     # opção é 1 faz a soma dos 2 números
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opção == 2:   # opção é 2 faz a sua multiplicação
        multi = n1 * n2
        print('A multiplicação entre {} x {} é {}'.format(n1, n2, multi))
    elif opção == 3:    # opção 3 difere qual número é maior ou não.
        if n1 > n2:
            maior = n1
        else:
            maior  = n2  
        print('Entre os dois valores exibidos, o maior é {}'.format(maior))
    elif opção == 4:  # Informar novos números
        print('Informe os números novamente...')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor:  '))
    elif opção == 5:  # Finalizar o programa. 
        print('FINALIZANDO...')      
    else:
        print('Opção inválida. Tente novamente!')
print('FIM DO PROGRAMA. OBRIGADO E VOLTE SEMPRE!')