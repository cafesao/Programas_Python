resposta = int()
string_arq = str()

nome_arq = str(input("\nPrimeiramente, escreva o caminho do seu arquivo: "))  
while True:
    print("\nO que você deseja fazer com o arquivo?")
    print('''
    [1] Ler o texto no arquivo
    [2] Substituir texto do arquivo
    [3] Adicionar texto ao arquivo
    [0] Sair
    ''')
    resposta = int(input("\n Opção: "))
    if resposta == 1:
        arq = open(nome_arq, "r")
        print("\n================================\n")
        print(arq.read())
        print("\n================================\n")
        arq.close()
    if resposta == 2:
        arq = open(nome_arq, "w")
        string_arq = str(input("Digite o que você quer colocar no texto:")) 
        print()
        arq.write(string_arq)
        arq.close()
    if resposta == 3:
        arq = open(nome_arq, "a")
        string_arq = str(input("Digite o que você quer adicionar ao texto: ")) 
        arq.write(string_arq)
        arq.close()
    if resposta == 0:
        break