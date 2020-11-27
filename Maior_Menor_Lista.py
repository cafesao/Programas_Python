lista1 = list()
for c in range (0,5):
    lista1.append(input('Digite um valor: (De 0 a 99)'))
max1 = max(lista1)
min1 = min(lista1)
print()
for c,v in enumerate(lista1):
    print(f'O valor {v} se encontra na posição {c}')
print(f'\nO maior numero é {max1} o menor é {min1}')