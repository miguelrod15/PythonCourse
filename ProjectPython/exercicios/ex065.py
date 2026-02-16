resposta = 'S'
soma = média = quant = 0
while resposta in 'Ss':
    num = int(input('Escreva um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print('Você escreveu {} números e a sua média foi {}'.format(quant, média))
print('O maior valor escrito foi {} e o menor foi {}'.format(maior, menor)) 
