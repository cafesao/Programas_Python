#Importa as bibliotecas
from random import randint

#Variaveis
numero_server = numero_user = cont_palpites = int()

#Funções
def retornar_valor_user():
    numero_user = int(input('Digite um numero (Entre 1 e 10): '))
    return numero_user

#Codigo
while True:
    numero_server = (randint(0,10))
    print('Adivinhe o numero! \n')
    numero_user = retornar_valor_user()
    print(numero_user)
    while numero_server != numero_user:
        print('\nVocê errou, tente de novo. \n')
        numero_user = retornar_valor_user()
        cont_palpites += 1
    print('\nParabéns você acertou!!')
    print(f'Foram necessários {cont_palpites} palpites para você acertar')     
    resposta = str(input('\nDeseja continuar o jogo? (Sim/Não): ')).split()[0].upper()        
    if resposta == 'N':
        break
print('\nObrigado por utilizar Adivinhação.')