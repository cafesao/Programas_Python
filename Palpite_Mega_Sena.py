# Mostra os palpites dos jogos da mega-sena, mostrandos os jogos no final.


listat = list()
from random import randrange
while True:
    n = int(input('Quantos jogos você vai fazer?: '))
    for p in range (1,n+1):
        listat = [randrange(0,60),randrange(0,60),randrange(0,60),randrange(0,60),randrange(0,60),randrange(0,60)]
        print(f'Jogo {p}: {listat}')
        listat.clear()
    r = str(input('\nDeseja fazer mais jogos? (Sim / Não):  ')).split()[0].capitalize()
    if r[0] == 'N':
        break