n1 = float(input('Escreve a primeira nota:'))
n2 = float(input('Escreve a segunda nota:'))
m = (n1 + n2)/2
print('A sua média deu {:.1f}'.format(m))
if m >= 6.0:
    print('A sua média foi boa!')
else:
    print('A sua média foi má, estude mais!')
