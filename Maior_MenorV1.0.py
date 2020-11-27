#Este programa tem a função de dizer qual o numero maior e qual o numero menor e, caso tenha igualdade, informar ao usuario.


while True:
    n1 = int(input('Digite um valor: '))
    n2 = int(input('Digite outro valor: '))
    if n1 > n2:
        print(f'O numero {n1} é maior que o numero {n2}, logo o segundo numero é maior')
    if n1 < n2:
        print(f'O numero {n2} é maior que o numero {n1}, logo o primeiro numero é maior')
    else:
        print('Não existe numeros maiores, os dois são iguais.')
    r = str(input('Deseja continuar? (Sim / Não): ')).split()[0].upper()
    if r[0] == 'N':
        break           
print('\nObrigado por utilizar o Maior e Menor.')