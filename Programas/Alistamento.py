# Este programa tem o intuito de dizer se o jovem tem que se alistar, se ja se alistou ou se passou o prazo de alistamento,
# mostrando também, quantos anos falta para ele se alistar.

nome_Informado = nome_Pronto = resposta = str()
ano_Pronto = ano_Informado = int()

while True:
    nome_Informado = str(input('Qual seu nome?: '))
    ano_Informado = int(input('Qual o ano do seu nascimento?: '))
    ano_Pronto = 2019 - ano_Informado
    nome_Pronto = nome_Informado.split()[0].capitalize()
    if ano_Pronto <= 18:
        print(f'{nome_Pronto}, você ainda não se alistou, faltam {18 - ano_Pronto} anos para vc se alistar. \n') 
    elif (ano_Pronto == 18):
        print(f'{nome_Pronto}, você deve se alistar este ano, fique atento! \n')
    else:
        print(f'{nome_Pronto}, passou o prazo de alistamento, verifique com a junta militar para regularizar sua situação. \n')         
    resposta = str(input('Deseja recomeçar? (Sim / Não): ')).split()[0].upper()
    if resposta[0] == 'N':
        break
print('\nObrigado por utilizar o Alistamento.')