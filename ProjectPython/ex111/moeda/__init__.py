def aumentar(preço=0, taxa=0, format=False):
    '''
    ->Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação
    :param preço: o preço que se quer reajustar 
    :param taxa: qual é porcentagem do aumento
    :param format: saída formatada ou não?
    :return: o valor reajustado , com ou sem formato.
    '''
    res = preço + (preço * taxa/100)
    return res if not format else moeda(res)

def diminuir(preço=0, taxa=0, format=False):
    res = preço - (preço * taxa/100)
    return res if not format else moeda(res)

def dobro(preço=0, format=False):
    res = preço * 2
    return res if not format else moeda(res)

def metade(preço=0, format=False):
    res = preço / 2
    return res if not format else moeda(res)

def moeda(preço=0, moeda='€'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')

def resumo(preço=0, taxa=20, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxa}% de aumento: \t{aumentar(preço, taxa, True)}')
    print(f'{taxar}% de redução: \t\t{diminuir(preço, taxa, True)}')
    print('-' * 30)