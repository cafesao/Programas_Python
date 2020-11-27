# Este e um programa um pouco mais completo, que pede a opção patra o usuario, incluindo o
# numero da opção

def opcoes():
    print('A seguir, leia o menu e selecione a opção desejada, digitando o numero correspondente.')
    print(''' 
    [1] Adição
    [2] Subtração       
    [3] Multiplicação   
    [4] Divisão
    [5] Potenciação   
    [0] Sair do programa \n''')

print('Bem-Vindo ao Menu de Matematica. \n')
while True:
    opcoes()
    op = int(input('Escolha a opção desejada: ')) 
    while op > 5:
        print('Você digitou uma opção errada, por favor, tente novamente. \n')
        opcoes()
        op = int(input('Escolha a opção desejada: ')) 
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    if op == 1:
        re = n1 + n2
        print(f'A soma entre os valores {n1} e {n2}, foi de {re} \n')
    if op == 2:
        re = n1 - n2
        print(f'A subtração entre os valores {n1} e {n2}, foi de {re} \n')
    if op == 3:
        re = n1 * n2
        print(f'A multiplicação entre os valores {n1} e {n2}, foi de {re} \n')
    if op == 4:
        re = n1 / n2
        print(f'A divisão entre os valores {n1} e {n2}, foi de {re:.5f} \n')
    if op == 5:
        re = n1 ** n2
        print(f'A potenciação entre os valores {n1} e {n2}, foi de {re} \n')    
    r = str(input('Deseja continuar? (Sim / Não): ')).split()[0].upper()
    if r[0] == 'N':
        break
print(' \nObrigado por usar o Menu!')