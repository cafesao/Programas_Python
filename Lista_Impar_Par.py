# Programa para adicionar numeros a lista, no final o programa mostra todos os valores,
# Os pares e os impares, em ordem.


listat = []
listap = []
listai = []
while True:
    n = int(input('Digite um numero: '))
    if n not in listat:
        listat.append(n)
        if (n%2) == 0:
            listap.append(n)
        else:
            listai.append(n)
    r = str(input('Deseja recomeçar? (Sim / Não): ')).split()[0].upper()
    if r[0] == 'N':
        break
listat.sort()
listap.sort()
listai.sort()
print(f'A lista de todos os numeros: {listat}')
print(f'A lista dos numeros pares: {listap}')
print(f'A lista dos numeros impares: {listai}')
print()