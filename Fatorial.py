


from math import factorial
while True:
    num1 = int(input('Digite o numero: '))
    f = factorial(num1)
    c = num1
    print(f'{num1}!= ', end='')
    while c > 0:
        print(f'{c}', end ='')
        print(' X ' if c > 1 else ' =', end ='')
        c = c - 1
    print(f' {f}')
    r = str(input('Deseja recomeçar? (Sim / Não): ')).split()[0].upper()
    if r[0] == 'N':
        break             
print('\nObrigado por utilizar Fatorial.')    