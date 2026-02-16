def readNumber(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERROR! PLEASE, TYPE A VALID INTEGER.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[031mUser interrupted data entry!\033[m')
            return 0
        else:
            return n

def readFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERROR! PLEASE, TYPE A VALID FLOAT')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUSER INTERRUPTED DATA ENTRY!\033[m')
            return 0
        else:
            return n

num = readNumber('Type an Integer: ')
num2 = readFloat('Type a Float: ')
print('-=' * 15)
print(f'The integer registered was {num} and the float was {num2}.')