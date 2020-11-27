from random import choice

palavras = ["COMER", "MUSICA", "BANANA", "CACHORRO", "GATO", "IMPRESSORA", "PANO", "ALICATE", "MOUSE", "PAPEL", "TECLADO", "MOUSEPAD", "MONITOR", "TELEVISAO", "JANELA", "CELULAR", "TELEFONE"]
letras_certas = []
letras_erradas = []
palavra_lista = []
erros = index = 0

def boneco_Inicio():
    print(""" 
    =========================Jogo da Velha========================
           -------------
           ⎜            ⎜
           ⎜            ⎜
           O            ⎜
          /⎜\           ⎜
         / ⎜ \          ⎜
          / \           ⎜
         /   \          ⎜
                        ⎜
                        ⎜
                     -------""")
def boneco_SemErro():
    print(f"""
    =========================Jogo da Velha========================
            -------------
            ⎜            ⎜
            ⎜            ⎜
                         ⎜
                         ⎜
                         ⎜
                         ⎜
                         ⎜
                         ⎜
                         ⎜
                      -------""")
def boneco_1Erro():
    print(""" 
    =========================Jogo da Velha========================
           -------------
           ⎜            ⎜
           ⎜            ⎜
           O            ⎜
                        ⎜
                        ⎜
                        ⎜
                        ⎜
                        ⎜
                        ⎜
                     -------""")
def boneco_2Erro():
    print(""" 
    =========================Jogo da Velha========================
           -------------
           ⎜            ⎜
           ⎜            ⎜
           O            ⎜
           ⎜            ⎜
                        ⎜
                        ⎜
                        ⎜
                        ⎜
                        ⎜
                     -------""")
def boneco_3Erro():    
    print(""" 
    =========================Jogo da Velha========================
           -------------
           ⎜            ⎜
           ⎜            ⎜
           O            ⎜
          /⎜            ⎜
                        ⎜
                        ⎜
                        ⎜
                        ⎜
                        ⎜
                     -------""")
def boneco_4Erro():
    print(""" 
    =========================Jogo da Velha========================
           -------------
           ⎜            ⎜
           ⎜            ⎜
           O            ⎜
          /⎜\           ⎜
                        ⎜
                        ⎜
                        ⎜
                        ⎜
                        ⎜
                     -------""")
def boneco_5Erro():
    print(""" 
    =========================Jogo da Velha========================
           -------------
           ⎜            ⎜
           ⎜            ⎜
           O            ⎜
          /⎜\           ⎜
             \          ⎜
                        ⎜
                        ⎜
                        ⎜
                        ⎜
                     -------""")
def boneco_6Erro():
    print(""" 
    =========================Jogo da Velha========================
           -------------
           ⎜            ⎜
           ⎜            ⎜
           O            ⎜
          /⎜\           ⎜
         /   \          ⎜
                        ⎜
                        ⎜
                        ⎜
                        ⎜
                     -------""")
def boneco_7Erro():
    print(""" 
    =========================Jogo da Velha========================
           -------------
           ⎜            ⎜
           ⎜            ⎜
           O            ⎜
          /⎜\           ⎜
         / ⎜ \          ⎜
                        ⎜
                        ⎜
                        ⎜
                        ⎜
                     -------""")
def boneco_8Erro():
    print(""" 
    =========================Jogo da Velha========================
           -------------
           ⎜            ⎜
           ⎜            ⎜
           O            ⎜
          /⎜\           ⎜
         / ⎜ \          ⎜
          /             ⎜
                        ⎜
                        ⎜
                        ⎜
                     -------""")
def boneco_9Erro():
    print(""" 
    =========================Jogo da Velha========================
           -------------
           ⎜            ⎜
           ⎜            ⎜
           O            ⎜
          /⎜\           ⎜
         / ⎜ \          ⎜
          /             ⎜
         /              ⎜
                        ⎜
                        ⎜
                     -------""")
def boneco_10Erro():
    print(""" 
    =========================Jogo da Velha========================
           -------------
           ⎜            ⎜
           ⎜            ⎜
           O            ⎜
          /⎜\           ⎜
         / ⎜ \          ⎜
          / \           ⎜
         /              ⎜
                        ⎜
                        ⎜
                     -------""")

while True:
    palavra = choice(palavras)
    numero_letra = int(len(palavra))
    boneco_Inicio()
    print("\nBem vindo ao JOGO DA VELHA, um jogo que exercita seu cerébro e te diverti, vamos jogar!!")
    resposta = str(input("\nDeseja jogar? (Sim / Não): ")).split()[0].upper()
    if resposta == 'S':
        palavra_secreta = str("#" * numero_letra)
        for c in palavra_secreta:
            palavra_lista.append(c)
        while True:
            if erros == 0:
                boneco_SemErro()
            if erros == 1:  
                boneco_1Erro()              
            if erros == 2:  
                boneco_2Erro()              
            if erros == 3:     
                boneco_3Erro()           
            if erros == 4:   
                boneco_4Erro()             
            if erros == 5: 
                boneco_5Erro()               
            if erros == 6:   
                boneco_6Erro()             
            if erros == 7: 
                boneco_7Erro()               
            if erros == 8:  
                boneco_8Erro()              
            if erros == 9:
                boneco_9Erro()                
            if erros == 10:
                boneco_10Erro()   
            if erros == 11:   
                boneco_Inicio()      
            if erros == 11:
                print("\nInfelizmente você perdeu, mais sorte da proxima vez :(")
                break  
            print(f"\nSua palavra tem {numero_letra} letras\n")
            verificacao = ''.join(map(str, palavra_lista))
            if verificacao in palavra:
                print("\nParabes, você conseguiu descobrir a palavra!")
                break 
            print(f"Palavra: {verificacao}")
            letras_certas_palavra = ','.join(map(str, letras_certas))
            letras_erradas_palavra = ','.join(map(str, letras_erradas))
            print(f"\nLetras certas: {letras_certas_palavra}")
            print(f"Letras erradas: {letras_erradas_palavra}")
            print("A qualquer momento você pode digitar EUSEI e responder toda a palavra, ", end="")
            print("caso acerte, você ganha, mas caso erre, infelizmente você perdera sem chance de tentar de novo.")
            resposta_letra = str(input("\nDigite a letra que você acha que é: ")).upper()
            if resposta_letra == 'EUSEI':
                resposta_letra = str(input("Olha, então me diga, qual a palavra?: ")).upper()
                if resposta_letra == palavra:
                    print("Uau, você conseguiu, parabens!")
                    break
                else:
                    print("Putz, você errou, mais sorte da proxima vez.")
                    break
            else:
                resposta_letra.split()[0]
            while True:
                if resposta_letra in letras_certas_palavra:
                    print("Você ja digitou esta letra.")
                    break
                if resposta_letra in letras_erradas_palavra:
                    print("Você ja digitou esta letra.")
                    break 
                if resposta_letra in palavra:         
                    letras_certas.append(resposta_letra)
                    for c in palavra:
                        index_palavra = c.find(resposta_letra)
                        if index_palavra == 0:
                            palavra_lista[index] = resposta_letra
                        index += 1
                    index = 0
                    break
                else:
                    print("Ops, não tem esta letra!")
                    letras_erradas.append(resposta_letra)
                    erros += 1
                    break
    else:
        break