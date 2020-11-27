pessoa = {}
pessoas = []
pessoasf = []
totalp = 0
totali = 0
while True:
    nome = str(input('Digite seu nome: ')).capitalize()
    idade = int(input('Digite sua idade: '))
    totali += idade
    sexo = str(input('Qual seu sexo (M - Masculino / F - Feminino): ')).split()[0].capitalize()
    if sexo == 'F':
        pessoasf.append(nome)
    pessoa['nome'] = nome
    pessoa['idade'] = idade
    pessoa['sexo'] = sexo
    pessoas.append(pessoa.copy())
    totalp += 1
    r = str(input('Deseja adicionar mais pessoas? (S - Sim / N -Não): ')).split()[0].capitalize()
    if r  == 'N':
        break
totali = totali / totalp
print(f'\nVocê adicionou {totalp} pessoas')
print(f'A media de idade é {totali:.0f}')
print(f'As mulheres cadastradas foram {pessoasf}\n')
print('Pessoas acima da media de idade: \n')
for c in pessoas:
    if c['idade'] > totali:
        for p,v in c.items():
            print(f'{p} = {v}')
        print()