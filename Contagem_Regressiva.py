# Contagem regressiva para o estouro dos fogos!

import time
while True:
    n1 = int(input('Digite um valor: '))
    for c in range(n1,0,-1):
        print(f'Vai estourar em: {c}')
        time.sleep(1)
    print('Os fogos estouraram!! \n')
    r = str(input('Deseja recomeçar? (Sim / Não): ')).split()[0].upper()
    if r[0] == 'N':
        break
print('\nObrigado por utilizar Contagem Regressiva.')
