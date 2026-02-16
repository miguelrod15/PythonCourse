from time import sleep
c = ('\033[m',                # 0 - without colors
     '\033[0;30;41m',         # 1 - red
     '\033[0;30;42m',         # 2 - green
     '\033[0;30;43m',         # 3 - yellow
     '\033[0;30;44m',         # 4 - blue
     '\033[0;30;45m',         # 5 - purple
     '\033[7;30m'             # 6 - white   
    );

def ajuda(com):
    title(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(1)

def title(msg, color=0):
    tam = len(msg) + 4
    print(c[color], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)

# Main Program
command = ''
while True:
    title('HELP SYSTEM PyHELP', 2)
    command = str(input("Function or Library > "))
    if command.upper() == 'FIM':
        break
    else:
        ajuda(command)
title('SEE YA', 1)