import os

def isPrime(n):
    if n <= 1:
        return False

    if n <= 3 or n == 5 or n == 7:
        return True

    primes = [2, 3, 5, 7]

    for i in primes:
        if n % i == 0:
            return False
        else:
            return True

def sys_clear():
    #Check Operating System
    #and send system command to clear terminal screen
    if os.uname().sysname == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def init():
    sys_clear()

    print('\n')

    num = int(input(' Enter a number: '))

    all_primes = []

    for i in range(num + 1):
        if isPrime(i) == True:
            all_primes.append(i)


    primes = str(all_primes)
    rows, n = '', ''
    count = 0

    for a in range(len(primes)):

        if primes[a].isdigit():
            n += primes[a]

        else:
            if count != 19:
                if n == '2' or n == '5':
                    rows += ' ' + n + '  '
                elif n == '9':
                    rows += ' ' + n + ' '
                else:
                    rows += n + ' '
                n = ''
                count += 1


            else:
                rows += n + '\n '
                n = ''
                count = 0



    #rows = rows[1:-1].replace('[', '')

    print('\n' + f' Prime Numbers from 2 to {str(num)}:\n\n ' + rows + '\n')

init()
