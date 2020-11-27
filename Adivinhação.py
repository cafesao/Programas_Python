# Este programa e uma versão melhorada do 'Adivinhação' ele pede para que o usuario 
# adivinhe o numero que o programa escolheu, de 1 a 10, repetindo quando o usuario erre

from random import randint

resposta = int(1)
numero_CPU = numero_JG = int()


while (resposta > 0):
    cont = 1
    numero_CPU = (randint(0,10))
    print('Adivinhe o numero \n')
    numero_JG = int(input('Digite um numero (Entre 1 e 10): '))
    while numero_CPU != numero_JG:
        print('\nVocê errou, tente de novo. \n')
        numero_JG = int(input('Digite um numero (Entre 0 e 10): '))
        cont = cont + 1
    if numero_JG == numero_CPU:
        print('\nParabéns você acertou!!')
        print(f'Foram necessários {cont} palpites para você acertar')
    print('\n[1] Repetir')
    print('[0] Finalizar \n')
    resposta = int(input('Digite a opção: '))              
print('\nObrigado por utilizar Adivinhação.')