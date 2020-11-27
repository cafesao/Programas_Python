


dados = list()
pessoas = list()
pmaior = list()
pmenor = list()
pmaior1 = pmenor1 = ptotal = 0
while True:
    dados.append(str(input('Digite seu nome: ')).capitalize())
    dados.append(float(input('Digite seu peso: ')))
    pessoas.append(dados[:])
    ptotal += 1
    dados.clear()
    r = str(input('Deseja adicionar mais pessoas (S - Sim / N - Não): ')).split()[0].upper()
    if r == 'N':
        break
for p in pessoas:
    if p[1] <= 46:
        pmenor1 += 1
        pmenor.append(p[0])
    if p[1] >=90:
        pmaior.append(p[0])
        pmaior1 += 1
print('Você adicionou as pessoas: ', end='')
for p in pessoas:
    print(p[0], end=', ')
print('.\n', end='')
print(f'Você adicionar {ptotal} pessoas.')
if pmaior1 >= 1:
    print(f'Dentre todas essas pessoas {pmaior1} são pesadas, são elas: {pmaior}',)
else:
    print('Não tem pessoas pesadas.')
if pmenor1 >= 1:
    print(f'Dentre todas essas pessoas {pmenor1} são leves, são elas: {pmenor}.')
else:
    print('Não tem pessoas leves.')
print()