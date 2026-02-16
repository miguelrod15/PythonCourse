valores = []
maior = 0
menor = 0

for c in range (0,5):
    valores.append(int(input(f'Escreva um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print('-=' * 20)
print(f'Escreveste os valores {valores}')
print('-=' * 20)

print(f'O maior valor dessa lista foi o número {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'E o menor valor foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
   if v == menor:
       print(f'{i}...', end='')
print()
