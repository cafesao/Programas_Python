# Este programa pede a informação de idade ao usuario e mostra a categoria que aquela idade corresponde.


while True:
    nom1 = str(input('Qual seu nome?: '))
    ida1 = int(input('Qual sua idade?: '))
    nom2 = nom1.split()[0].capitalize()
    if ida1 <= 9:
        print(f'Sr.(a) {nom2} esta classificada(o) como Mirim. \n')
    elif (ida1 >= 10) and (ida1 < 14):
        print(f'Sr.(a) {nom2} esta classificada(o) como Infantil \n')
    elif (ida1 >= 15) and (ida1 < 19):
        print(f'Sr.(a) {nom2} esta classificada(o) como Junior \n')
    elif ida1 == 20:
        print(f'Sr.(a) {nom2} esta classificada(o) como Sênior \n') 
    else:
        print(f'Sr.(a) {nom2} esta classificada(o) como Master \n') 
    r = str(input('Deseja recomeçar? (Sim / Não): ')).split()[0].upper()
    if r[0] == 'N':
        break            
print('\nObrigado por utilizar Natação.')