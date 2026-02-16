distância = float(input('Qual é a distância da sua viagem?:'))
print('A distância tem {}Km'.format(distância))

preço = distância * 0.5 if distância <= 200 else distância * 0.45 
print('O preço da sua passagem será EUR${:.2f}'.format(preço))