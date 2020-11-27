from random import randrange

while True:
    tuple1 = (randrange(0,6),randrange(0,6),randrange(0,6),randrange(0,6),randrange(0,6))
    max1 = max(tuple1)
    min1 = min(tuple1)
    print(f'A lista de numeros {tuple1}, o maior numero {max1} e o menor {min1}')
    re = str(input('Deseja refazer? (S - Sim / N - Não): ')).split()[0].upper()
    if re == 'N':
        break
print('Obrigado por utilizar os numeros sorteados.')
