print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Qual valor deseja levantar?: €'))
total = valor 
notas = 50
totnotas = 0
while True:
    if total >= notas:
        total -= notas
        totnotas += 1
    else:
        if totnotas > 0:
            print(f'Total de {totnotas} notas de €{notas}')
        if notas == 50:
            notas = 20
        elif notas == 20:
            notas = 10
        elif notas == 10:
            notas = 1
        totnotas = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao Banco CEV! Tenha um bom dia.')