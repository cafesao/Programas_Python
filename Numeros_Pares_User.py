# Soma todos os numeros pares

c = int(1)
while (c > 0):
        n2 = 0
        for c in range(0,6):
            n1 = int(input('Digite um valor: '))
            if (n1 % 2) == 0:
                n2 = n2 + n1
        print(f'A soma dos numeros pares foi de: {n2}')
        print('\n[1] Repetir')
        print('[0] Finalizar \n')
        c = int(input('Digite a opção: '))              
        print('\nObrigado por utilizar Numeros Pares.')