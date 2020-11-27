#Codigo
while True:
    nome_user = str(input('Qual seu nome?: ')).split()[0].capitalize()
    ano_nascimento = int(input('Qual o ano do seu nascimento?: '))
    ano_nascimento = 2019 - ano_nascimento
    if ano_nascimento < 18:
        print(f'{nome_user}, você ainda não se alistou, faltam {18 - ano_nascimento} anos para vc se alistar. \n') 
    elif ano_nascimento == 18:
        print(f'{nome_user}, você deve se alistar este ano, fique atento! \n')
    else:
        print(f'{nome_user}, passou o prazo de alistamento, verifique com a junta militar para regularizar sua situação. \n')         
    resposta = str(input('Deseja recomeçar? (Sim / Não): ')).split()[0].upper()
    if resposta == 'N':
        break
print('\nObrigado por utilizar o Alistamento.')

#Exemplo sem declarar ANTES nenhuma variavel