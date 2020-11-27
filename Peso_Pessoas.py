# Mostra o maior e o menor peso da pessoa informada.


maior = 1
menor = 1000
pe = int(input('Quantas pessoas você quer adicionar?: '))
for c in range(1,pe+1):
    peso = float(input(f'Qual o peso da {c} pessoa?: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso  
print(f'O maior peso foi {maior} e o menor peso foi {menor}')          