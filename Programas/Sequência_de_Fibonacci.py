# Este programa mostra a sequência de Fibonnaci, perguntando ao usuario o numero de termos
# que ele deseja, e repetindo tudo de novo caso ele queira

ve = re = a = 0
n2 = 2
b = c = 1
while (c > 0):
    ve = int(input('Digite um numero: '))
    print(f'\n{a} -> {b}', end='')
    while (ve-1 >= n2):
        re = a + b
        print(f' -> {re}', end='')
        a = b
        b = re
        n2 = n2 + 1
    print('\nFim da seguência')
    res = str(input('\nDeseja fazer de novo? (S/N)').split()[0].upper())
    if res == 'S':
        c = 1
    if res == 'N':
        c = 0    
print('\nObrigado por utilizar a Seguência de Fibonacci.')    