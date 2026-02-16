peso = float(input('Qual é o seu peso?: (Kg)'))
altura = float(input('Qual é a sua altura? (m)'))
imc = peso / altura ** 2
print('O IMC correspondente é {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= imc < 25:
    print('Peso ideal!')
elif 25 <= imc < 30:
    print('Sobrepeso!!')
elif 30 <= imc < 40:
    print('OBESIDADE!')
elif imc >= 40:
    print('Obesidade mórbida!')
