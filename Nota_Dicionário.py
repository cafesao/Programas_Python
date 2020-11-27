aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: ')).capitalize()
aluno['media'] = int(input('Digite a media do aluno: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
if aluno['media'] < 7:
    aluno['situação'] = 'Reprovado'
print(f'O aluno {aluno["nome"]} com a media {aluno["media"]} foi {aluno["situação"]}')