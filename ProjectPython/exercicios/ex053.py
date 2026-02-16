frase = str(input('Escreva uma frase: ')).strip().upper()  # Meter a frase em CAPS
palavras = frase.split()  # Dividir a frase em uma lista
junto = ''.join(palavras)  # Juntar as palavras da lista sem espaços
inverso = ''               # Fazer o inverso da frase

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
    print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos uma CAPICUA')
else:
    print('Não temos uma CAPICUA')  