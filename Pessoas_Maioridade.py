# Mostra entre as 7 pessoas, quantas pessoas são maiores de idade.


num1 = 0
for c in range(0,7):
    pe1 = int(input('Digite o ano de nascimento: '))
    pe1 = 2019 - pe1
    if pe1 >= 21:
        num1 = num1 + 1
print(f'Entre as 7 pessoas, {num1} pessoas são maiores de idade.')