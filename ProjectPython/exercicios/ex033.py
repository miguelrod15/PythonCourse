a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))

# Verificando quem é o menor número
menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c

# Verificando quem é o maior número
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c

print('O menor valor digitado foi o {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))