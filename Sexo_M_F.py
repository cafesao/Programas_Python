# Pede ao user que selecione entre M e F, e depois, o programa mostra se for digitado M,
# Mosgtra que é masculino, e se for F mostra que é feminino, tendo também, uma mensagem
# De erro caso escreva outra coisa.


s = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
while s not in 'MF':
    s = str(input('Digite o sexo corretamente: [M/F] ')).strip().upper()[0]
if s == 'M':
    print('Você digitou Masculino, esta correto.')
else:
    print('Você digiou Feminino, esta correto.')    