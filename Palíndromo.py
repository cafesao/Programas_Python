# Mostra se a frase é um Palíndromo ou não
# (Frase que tem o mesmo significado de trás para frente).


frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1,-1,-1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print(f'A frase: {frase}, é um Palíndromo')
else: 
    print('Esta frase não é um Palíndromo')    