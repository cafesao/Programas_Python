tuple1 = ('Banana','Garrafa','Capital','Sidney','Maria','Notebook','Coisa','Teclado','Mouse','Algo')
for p in tuple1:
    print(f'\nNa palavra {p.upper()} temos: ', end = '')
    for letra in p:
        if letra in ('aeiou'):
            print(letra, end = ' ')
print()
