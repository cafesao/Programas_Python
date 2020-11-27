# Pede ao user o primeiro termo e a razão, tendo essas informações, o programa faz a PA.


t1 = int(input('Digite o Primeiro Termo: '))
r1 = int(input('Digite a Razão: '))
n = 1
c = 9
print(f'\nTermo 1 : {t1}')
while (c > 0):
    t1 = t1 + r1
    n = n + 1
    c = c - 1
    print(f'Termo {n} : {t1}')
print('Foi apresentando 10 termos')    
re = str(input('Deseja mostrar mais temos? (S/N)')).split()[0].upper()
if re == 'S':
    c = int(input('\nDigite quantos termos você quer a mais: '))
    while (c > 0):
        t1 = t1 + r1
        n = n + 1
        c = c - 1
        print(f'Termo {n} : {t1}') 
else:
    print('\nObrigado por utilizar o PA')
    exit  