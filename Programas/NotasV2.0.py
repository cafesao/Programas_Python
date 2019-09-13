#Lançamento e impressão (Fictícia) das notas de um ou mais alunos

from tabulate import tabulate
alunos = []
dados = []
alunosc = []
alunost = media = 0
print('Bem-Vindo ao programa Media_Notas V2.0\n')
escola = str(input('Digite o nome da escola: ')).capitalize()
serie = str(input('Digite a serie: '))
while True:
    a = str(input('\nDigite o nome do aluno: ')).capitalize()
    dados.append(a)
    for c in range (0,4):
        n = float(input('Digite a nota do aluno: '))
        dados.append(n)
    alunos.append(dados[:])
    dados.clear()
    r = str(input('Deseja adicionar mais alunos? (Sim / Não): ')).split()[0].upper()
    if r[0] == 'N':
        break
for t in alunos:
    alunost += 1
    media = (t[1] + t[2] + t[3] + t[4]) / 4
    print(f'O aluno {t[0]} tirou as seguintes notas: {t[1]} : {t[2]} : {t[3]} : {t[4]}')
    print(f'A media foi: {media:.2f}')
    print('')
while True:
    r = str(input('Deseja emitir o boletim dos alunos? (Sim/Não): '))
    if r[0] == 'N':
        break
    print('''
[1] Todos os alunos
[2] Aluno Específico''')
    r = int(input('\nDeseja emitir o boletim de todos os alunos ou de algum especifico: '))
    if r == 2:
        print(f'No sistema tem {alunost} alunos')
        print(f'Os alunos são: \n')
        alunost = 0 
        for t in alunos:
            print(f'{alunost} - {t[0]} ')
            alunost += 1
        r = int(input('\nQual aluno você deseja: '))
        media = (alunos[r][1] + alunos[r][2] + alunos[r][3] + alunos[r][4]) / 4
        if media >= 6:
            aprov = 'Aprovado'
        if media < 6:
            aprov = 'Não Aprovado'
        print(f'''
---------------------------------------------------------
Escola: {escola}
Serie: {serie}
Nome: {alunos[r][0]} 
---------------------------------------------------------
        1º Bi        2º Bi       3º Bi       4º Bi
Notas:   {alunos[r][1]}          {alunos[r][2]}         {alunos[r][3]}         {alunos[r][4]}
---------------------------------------------------------
Media: {media:.2f}
Aprovação: {aprov}
---------------------------------------------------------
''')
        print()
        break
    if r == 1:
        for b in alunos:             
            media = (b[1] + b[2] + b[3] + b[4]) / 4
            if media >= 6:
                aprov = 'Aprovado'
            if media < 6:
                aprov = 'Não Aprovado'
            print(f'''
---------------------------------------------------------
Escola: {escola}
Serie: {serie}
Nome: {b[0]} 
---------------------------------------------------------
        1º Bi        2º Bi        3º Bi      4º Bi
Notas:   {b[1]}          {b[2]}         {b[3]}         {b[4]}
---------------------------------------------------------
Media: {media:.2f}
Aprovação: {aprov}
---------------------------------------------------------
''')
    break