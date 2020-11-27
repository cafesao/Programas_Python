# Este programa funciona como um jogo de Par ou Impár, com varios if dentro de uma estrutura
# de repetição com uma flag


import random
j1 = c2 = re = pi = 0
lista1 = [2,4]
lista2 = [1,3,5]
lista3 = [1, 2, 3, 4, 5]
stop = ''
print('Este e a brincadeira do Par ou Impár!')
while True:
    j1 = int(input('\nDigite um valor de 1 a 5: '))
    if j1 in lista1:
        pi = 1 # Pi = Ele diz ao programa se o user escolheu par ou impar
        c2 = random.choice(lista3)
    if j1 in lista2:
        pi = 2 # Pi = Ele diz ao programa se o user escolheu par ou impar
        c2 = random.choice(lista3)
    re = j1 + c2
    if (re%2) == 0:
        if pi == 1:
            print(f'Você ganhou! o resultado foi {re}, o computador escolheu {c2}')
        if pi == 2:
            print(f'Você perdeu, o resultado foi {re}, o computador escolheu {c2}')
    else:
        if pi == 2:
            print(f'Você ganhou! o resultado foi {re}, o computador escolheu {c2}')
        if pi == 1:
            print(f'Você perdeu, o resultado foi {re}, o computador escolheu {c2}')
    stop = str(input('\nDeseja recomeçãr? (S - SIM / N - NÃO): ').split()[0].upper())
    if stop in 'N':
        break
print('\nObrigado por utilizar o jogo do Par ou Impár')