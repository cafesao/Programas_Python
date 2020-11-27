# Este programa mostra o IMC, pedindo ao user a altura e o peso.


while True:
    nom1 = str(input('Qual seu nome?: '))
    alt1 = float(input('Qual sua altura?: '))
    pes1 = float(input('Qual seu peso?: '))
    nom2 = nom1.split()[0].capitalize()
    imc =  pes1 / (alt1 ** 2)
    if imc < 18.5:
        print(f'Sr.(a) {nom2}, seu IMC foi de {imc:.2f}, você esta abaixo do peso, se alimente!')
    elif (imc >= 18.5) and (imc < 25):
        print(f'Sr.(a) {nom2}, seu IMC foi de {imc:.2f}, você esta com o peso ideal, parabens!')
    elif (imc >= 25) and (imc < 30):
        print(f'Sr.(a) {nom2}, seu IMC foi de {imc:.2f}, você esta com sobrepeso, cuidado!')
    elif (imc >= 30) and (imc < 40):
        print(f'Sr.(a) {nom2}, seu IMC foi de {imc:.2f}, você esta com obesidade, tenha muito cuidado!')
    else:       
        print(f'Sr.(a) {nom2}, seu IMC foi de {imc:.2f}, você esta com obesidade mórbida, procure um medico imediatamente!')   
    r = str(input('Deseja recomeçar? (Sim / Não): ')).split()[0].upper()
    if r[0] == 'N':
        break  
print('\nObrigado por utilizar IMC.')