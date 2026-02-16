palavras = ('Aprender', 'Jogar', 'Brincar', 'Python',
            'curso', 'programar', 'estudar', 'trabalhar',
            'Obedecer', 'Deus', 'Planta', 'Bola')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')