def readNumber(msg):
    while True:
        number = input(msg)
        if number.isnumeric():
            return int(number) 
        else:
            print('\033[031mERROR! Enter a valid integer.\033[m')

# Main program
n = readNumber('Enter an integer: ')
print(f'You just typed the number {n}')