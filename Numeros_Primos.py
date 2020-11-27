# Mostra se o numero é primo ou não.


n1 = int(input('Digite um valor: '))
n2 = 0
n3 = 0
for c in range(0,n1+1):
    n2 = n2 + 1
    if (n1 % n2) == 0:
        n3 = n3 + 1
if (n3) == 2:
    print(f'O numero {n1} é primo')
else:
    print(f'O numero {n1} não é primo')    