nr = int(0)
tuple1 = ( int(input('Digite o primeiro valor: ')),
    int(input('Digite o segundo valor: ')),
    int(input('Digite o terceiro valor: ')),
    int(input('Digite o ultimo valor: ')))
for n in tuple1:
    if n % 2 == 0:
        nr += 1
if 9 in tuple1:
    count1 = tuple1.count(9)
    print(f'\nO numero 9 apareceu {count1} vez')
else:
    print('\nO numero 9 não apareceu')
if 3 in tuple1:
    index1 = tuple1.index(3)
    print(f'O numero 3 foi digitado na posição {index1}')
else: 
    print('Não tem numero 3')
if nr == 1:
    print(f'Dentre todos esses numeros {nr} é par\n')
elif nr > 1:
    print(f'Dentre todos esses numeros {nr} são pares\n')
else:
    print('Não tem numeros pares.\n')